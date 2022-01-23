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

from entries import views as entries_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("entries/new", entries_views.new_entry_view, name="new_entry"),
    path("entries", entries_views.entry_log_view, name="entries_log"),
    path("entries/summary", entries_views.summary_view, name="summary"),
    path("entries/edit/<pk>", entries_views.EntryEditView.as_view(), name="edit"),




]
