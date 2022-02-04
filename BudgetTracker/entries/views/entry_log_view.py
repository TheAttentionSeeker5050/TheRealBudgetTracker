# view related imports
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# import the models
from entries.models import Entry

# import the forms
from entries.forms import EntryForm

# import time functions
from django.utils import timezone


def entry_log_view(request):
    this_month = timezone.now().month
    this_year = timezone.now().year
    return redirect("entries/{}/{}".format(this_year, this_month))
   


from django.views.generic.dates import MonthArchiveView
from django.views.generic.dates import MonthMixin

class EntryMonthLogView(MonthArchiveView, MonthMixin):
    queryset = Entry.objects.all()
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

