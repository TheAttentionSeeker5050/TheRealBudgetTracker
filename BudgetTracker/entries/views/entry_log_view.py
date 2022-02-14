# view related imports
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect


# login required
# from users.views import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin


# import the models
from entries.models import Entry

# import the forms
from entries.forms import EntryForm

# import time functions
from django.utils import timezone

def entry_log_view(request):
    this_month = timezone.now().month
    this_year = timezone.now().year

    if request.user.is_authenticated:

        return redirect("entries/{}/{}".format(this_year, this_month))
    else:
        return redirect("login")
   


from django.views.generic.dates import MonthArchiveView
from django.views.generic.dates import MonthMixin

class EntryMonthLogView(LoginRequiredMixin, MonthArchiveView, MonthMixin):
    """Displays all the logs made by the current user in a specific month"""
    login_url = "/login"
    redirect_field_name = "login"
    
    date_field = "date"
    allow_future = True
    template_name = "entries/entries_log.html"
    allow_empty = True

    def dispatch(self, request, *args, **kwargs):
        """Here we get the values of the url tags """
        self.year = kwargs["year"]
        self.month = kwargs["month"]
        
        return super(EntryMonthLogView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Here we get the values of the url tags
        """
        data = super(EntryMonthLogView, self).get_context_data(**kwargs)

        data["month"] = self.month
        data["year"] = self.year
        return data

    def get_queryset(self):
        return Entry.objects.filter(username=self.request.user)
