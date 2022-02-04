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
from django.urls import path

from entries.views import views as entries_views
from django.conf.urls.static import static
from django.conf import settings

from entries.views import add_edit_view


app_name = 'entries'

urlpatterns = [
    # admin url
    path('admin/', admin.site.urls),

    # add and edit view url
    path("entries/new", add_edit_view.new_entry_view, name="new_entry"),
    path("entries/edit/<pk>", add_edit_view.EntryEditView.as_view(), name="edit"),
    
    # delete view url
    path('entries/delete/<pk>', entries_views.EntryDeleteView.as_view(), name="delete"),

    path("entries/summary", entries_views.summary_view, name="summary"),
    path("entries/summary/<int:year>/<int:month>/", entries_views.SummaryMonthView.as_view(month_format="%m"), name="summary_by_month"),
    path("entries", entries_views.entry_log_view, name="entries_log"),
    path('entries/<int:year>/<int:month>/',
         entries_views.EntryMonthLogView.as_view(month_format='%m'),
         name="log_by_month"),
    
    
    




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
