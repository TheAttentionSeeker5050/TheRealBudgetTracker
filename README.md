# TheRealBudgetTracker



This is a basic expense tracker app. That will get more complex as we go.

# Version 1.1
Chart options for the summary page were added. This new iteration also has custom search options for the entries, a login, register and authentication system and it only displays entries made by the user.

## Actual features
The main features in release 1.0 include:

- All features of version 1.0
- Login and register system and authentication
- Expense and income by category js charts
- Refined Rest API
- Search options for entries
- Fixed bugs on class based views

## Known bugs

- I still need to do the testing. I will be working in a few other projects. Feel proud of what I have done, there is still room for improvements, like adding more options, more responsiveness and a mobile option.



# Version 1.0
Consist on the minimal working program. I'm working on separating backend to frontend at this moment

## Actual features
The main features in release 1.0 include:

- Add new entries in both income and expenses
- Visualize the income and expense logs
- A database including category, description, date and amount
- A quick summary per month, nothing fancy
- Serving static files
- Filter buttons

# General notes

## Features that will be added in the future

- Add a photo of the receipt 
- Debts, bills and push notifications
- Asset  and investments values
- A quick balance sheet, as I said, nothing fancy
- Simulators (i.e. debt repayment, compound interest, loan amortization)
- Real time market watch
- Share button and download options (pdf, spreadsheets, csv)
- Postgres database system



## Libraries, technologies and frameworks I'm using

- Still using sqlite3, but I will switch to postgres later. I have done it before, I just don't want to bother at this moment
- I got the mock data from a website called Mockaroo
- Django (dah!!?)
- There is no need for a frontend framework, I can do fine with vanilla js on the frontend
- Django rest framework
- A js chart library called Charts.js
- Django class based views
