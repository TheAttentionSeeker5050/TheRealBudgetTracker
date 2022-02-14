"""BudgetTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

from entries.views import add_edit_view
from entries.views import entry_log_view
from entries.views import summary_view
from entries.views import delete_view
from entries.views import api_view

from users.views import UserLoginView, SignUpView, LogoutView

router = routers.DefaultRouter()
router.register(r'entries/$', api_view.EntryApiViewSet,  basename='get_entry_data')
# router.register(r'entries/{username}/', api_view.EntryApiView.as_view())



app_name = 'entries'

urlpatterns = [
    # admin url
    path('admin/', admin.site.urls),

    # add and edit view url
    path("entries/new", add_edit_view.CreateEntryView.as_view(), name="new_entry"),
    path("entries/edit/<pk>", add_edit_view.EntryEditView.as_view(), name="edit"),
    
    # delete view url
    path('entries/delete/<pk>', delete_view.EntryDeleteView.as_view(), name="delete"),

    # summary url
    path("entries/summary", summary_view.summary_view, name="summary"),
    path("entries/summary/<int:year>/<int:month>/", summary_view.SummaryMonthView.as_view(month_format="%m"), name="summary_by_month"),
    
    # entry log view
    path("entries", entry_log_view.entry_log_view, name="entries_log"),
    path('entries/<int:year>/<int:month>/',
         entry_log_view.EntryMonthLogView.as_view(month_format='%m'),
         name="log_by_month"),
    
    # path('api/entries/', api_view.EntryApiView.as_view( )),
    path('api_call/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("api/entries/", api_view.EntryList.as_view(), name="entries_api_call"),
    path("api/entries/<int:year>/<int:month>/", api_view.EntryListByYear.as_view(), name="entries_api_call"),




    # home page 
    # path("", views.homepage, name="homepage"),
    
    # user authentication
    path("login", UserLoginView.as_view(), name="login"),
    path("register", SignUpView.as_view(), name="register"),
    path("logout", LogoutView.as_view(), name= "logout"),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
