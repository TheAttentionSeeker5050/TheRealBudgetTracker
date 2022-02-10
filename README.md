# TheRealBudgetTracker



This is a basic expense tracker app. That will get more complex as we go.


# Version 1.0
Consist on the minimal working program. I'm working on separating backend to frontend at this moment

## Actual features
Its main features in release 1.0 include:

- Add new entries in both income and expenses
- Visualize the income and expense logs
- A database including category, description, date and amount
- A quick summary per month, nothing fancy
- Serving static files
- Filter buttons


## Features that will be added in the future
- Full React-Django integration
- Add a photo of the receipt 
- Debts, bills and push notifications
- Asset  and investments values
- A quick balance sheet, as I said, nothing fancy
- Simulators (i.e. debt repayment, compound interest, loan amortization)
- Real time market watch
- Share button and download options (pdf, spreadsheets, csv)


## Known bugs

- I'm still figuring out how to add a js chart functionality
- The rest api is not there yet
- This is a backend only application. In the future when I get the rest framework working I will add a React backend. Probably an android app too. We'll see.
- As I stated the previous point, I will get rid of the django templates for something more on the front end. That will give me the freedom to make an app style website.

## Libraries, technologies and frameworks I'm using

- Still using sqlite3, but I will switch to postgres later. I have done it before, I just don't want to bother
- I got the mock data from a website called Mockaroo
- Django (dah!!?)
- I will add react in the future
- Django rest framework in which I'm working on at this moment
- A js chart library called Charts.js
- Django class based views
- I am using the vanilla django templates at this moment
- Vanilla JS for the filter buttons and whatnot, but will transform all that to react
