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

from django.conf.urls.static import static
from django.conf import settings

from entries.views import add_edit_view
from entries.views import entry_log_view
from entries.views import summary_view
from entries.views import delete_view





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
    
    
    




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
