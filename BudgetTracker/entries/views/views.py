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

# Create your views here.



# def new_entry_view(request):
#     """This is the default new entry view"""

#     # if it is a post we need to request the input data
#     if request.method == "POST":
#         # create a post instance and populate it with the data from the request
#         form = EntryForm(request.POST)

#         if form.is_valid():
#             # Processs the date in the form and return cleaned data
#             entry_type = form.cleaned_data["entry_type"]
#             description = form.cleaned_data["description"]
#             category = form.cleaned_data["category"]
#             date = form.cleaned_data["date"]
#             amount = form.cleaned_data["amount"]

#             # we save the cleaned data
#             q = Entry(entry_type=entry_type, description=description, category=category, date=date, amount=amount)
#             q.save()
#             return redirect("entries_log")

#     # or if a get well create a blank form
#     else:
#         form = EntryForm()


#     return render(request, "entries/new.html", {"form":form})

def entry_log_view(request):
    this_month = timezone.now().month
    this_year = timezone.now().year
    return redirect("entries/{}/{}".format(this_year, this_month))
    

def summary_view(request):
    """Redirects to a basic financial summary of the person's expenses and incomes for the current month"""
    
    this_month = timezone.now().month
    this_year = timezone.now().year

    return redirect("summary/{}/{}".format(this_year, this_month))

# from django.views.generic.edit import UpdateView

# class EntryEditView(UpdateView):
#     """Edit an existing entry"""
#     template_name = 'entries/edit.html'
#     model = Entry
#     fields = ['entry_type', "description", "category", "date", "amount"]
#     success_url = "/entries"

# import delete class based view 
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

class EntryDeleteView(DeleteView):
    """Our delete entry view"""
    # define our model
    model = Entry

    # the template
    template_name = "entries/delete.html"
    context_object_name = 'deleteview'

    def get_success_url(self):
        # return a redirection
        return reverse_lazy('entries_log')

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


from itertools import chain
from django.db.models import Sum
import decimal
# from django.db.models import Case, Value, When, IntegerField

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

        from django.db.models.functions import Round

        # now we display the categories to make the pie charts
        expense_categories_labels = ["Food", "Housing", "Transportation", "Fun & Entertainment", "Investing", "Interest & Debts"] 
        expense_categories_amounts = []

        for category in expense_categories_labels:
            expense_categories_amounts.append(Entry.objects.all().filter(entry_type="Expense", date__year=self.year,  date__month=self.month, category=category).aggregate(Sum("amount"))["amount__sum"])
            # print(temp_var)

            

        income_categories_labels = ["Allowance", "Work", "Investment Returns"] 
        
        income_categories_amounts = []

        for category in income_categories_labels:
            income_categories_amounts.append((Entry.objects.all().filter(entry_type="Income", date__year=self.year, date__month=self.month, category=category).aggregate(Sum("amount"))["amount__sum"]))

        print(expense_categories_amounts)
        print(income_categories_amounts)


        data["income"] = total_income
        data["expense"] = total_expense
        data["balance"] = balance
        data["month"] = self.month
        data["year"] = self.year
        data["expense_categories_labels"] = expense_categories_labels
        data["expense_categories_amounts"] = expense_categories_amounts
        data["income_categories_labels"] = income_categories_labels
        data["income_categories_amounts"] = income_categories_amounts
        return data

