import React, { Component } from "react";

import {EntriesLog, EntryItem} from './EntriesLog';

const entry_list = [{
  "id": 1,
  "username": "User",
  "entry_type": "Expense",
  "description": "Beauty",
  "category": "Fun & Entertainment",
  "date": "2021-06-24",
  "amount": "387.20"
},
{
  "id": 2,
  "username": "User",
  "entry_type": "Income",
  "description": "Garden",
  "category": "Investment Returns",
  "date": "2021-04-29",
  "amount": "550.32"
},
{
  "id": 3,
  "username": "User",
  "entry_type": "Expense",
  "description": "Outdoors",
  "category": "Fun & Entertainment",
  "date": "2021-05-24",
  "amount": "310.45"
},
{
  "id": 4,
  "username": "User",
  "entry_type": "Expense",
  "description": "Electronics",
  "category": "Allowance",
  "date": "2021-02-05",
  "amount": "503.98"
},
{
  "id": 5,
  "username": "User",
  "entry_type": "Expense",
  "description": "Movies",
  "category": "Food",
  "date": "2021-07-04",
  "amount": "530.23"
},
{
  "id": 6,
  "username": "User",
  "entry_type": "Income",
  "description": "Toys",
  "category": "Food",
  "date": "2021-10-08",
  "amount": "873.04"
},
{
  "id": 7,
  "username": "User",
  "entry_type": "Expense",
  "description": "Shoes",
  "category": "Allowance",
  "date": "2022-01-28",
  "amount": "339.05"
},
{
  "id": 8,
  "username": "User",
  "entry_type": "Expense",
  "description": "Tools",
  "category": "Work",
  "date": "2021-04-20",
  "amount": "204.12"
},
{
  "id": 9,
  "username": "User",
  "entry_type": "Income",
  "description": "Baby",
  "category": "Investment Returns",
  "date": "2021-12-07",
  "amount": "750.40"
},
{
  "id": 10,
  "username": "User",
  "entry_type": "Expense",
  "description": "Jewelry",
  "category": "Investing",
  "date": "2021-02-09",
  "amount": "992.79"
},
{
  "id": 11,
  "username": "User",
  "entry_type": "Income",
  "description": "Sports",
  "category": "Investment Returns",
  "date": "2021-12-10",
  "amount": "835.46"
},
{
  "id": 12,
  "username": "User",
  "entry_type": "Expense",
  "description": "Clothing",
  "category": "Investing",
  "date": "2021-05-17",
  "amount": "625.03"
}
]

function AppBody() {
    return (
      <div className="app_body">
        <EntriesLog>
          {entry_list.map(
            (entry) => (
              <EntryItem
                entry_type={entry.entry_type}
                description={entry.description}
                category={entry.category}
                date={entry.date}
                amount={entry.amount}
              />
            )
          )}

        </EntriesLog>
      </div>
    );
  }

export {AppBody};