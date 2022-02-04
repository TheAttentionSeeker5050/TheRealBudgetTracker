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

# import the date views mixins

from django.views.generic.dates import MonthArchiveView
from django.views.generic.dates import MonthMixin

def summary_view(request):
    """Redirects to a basic financial summary of the person's expenses and incomes for the current month"""
    
    this_month = timezone.now().month
    this_year = timezone.now().year

    return redirect("summary/{}/{}".format(this_year, this_month))


class SummaryMonthView(MonthArchiveView):
    """We only show the summary for the month specified in the url"""
    
    
    context_object_name = "data"
    date_field = "date"
    allow_future = True
    template_name = "entries/summary.html"
    allow_empty = True
    queryset = Entry.objects.all()

    def dispatch(self, request, *args, **kwargs):
        """Here we get the values of the url tags """
        self.year = kwargs["year"]
        self.month = kwargs["month"]
        
        return super(SummaryMonthView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Lets do the summary logic here. We do the sum of the total income and balance for the current month
        that is stated in the url
        """
        
        data = super(SummaryMonthView, self).get_context_data(**kwargs)
        
        
        all_income = Entry.objects.all().filter(entry_type="Income", date__year=self.year, date__month=self.month)
        all_expense = Entry.objects.all().filter(entry_type="Expense", date__year=self.year, date__month=self.month)

        total_income=0
        total_expense=0

        for entry in all_income:
            total_income = entry.amount + total_income
        
        for entry in all_expense:
            total_expense = entry.amount + total_expense



        balance = total_income - total_expense



        data["income"] = total_income
        data["expense"] = total_expense
        data["balance"] = balance
        data["month"] = self.month
        data["year"] = self.year
        
        return data

