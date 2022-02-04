from entries.views.APIViewSet import api_entries_view_list, request_all_entries
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
# from rest_api import views

# router = DefaultRouter()
# router.register()
# router.register(r'/', request_all_entries, basename='entry')

urlpatterns = [
    re_path(r'<int:year>/<int:month>', api_entries_view_list, basename='entry'),
    re_path(r'/', request_all_entries, basename='entry'),
]