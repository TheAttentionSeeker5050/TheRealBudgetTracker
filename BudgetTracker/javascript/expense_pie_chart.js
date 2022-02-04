// first we import our random color generator
import {generate_random_color} from "./generate_random_color.js";

// we get the canvas element by id
const ctx = document.getElementById('expense_pie_chart').getContext('2d');

const config = {
    type: 'pie',
    data: data_expense,
  };

// we get the income and expense label array
const expense_categories_labels = JSON.parse(document.getElementById("expense_categories_labels").innerHTML)

const income_categories_labels = JSON.parse(document.getElementById("income_categories_labels").innerHTML)

// we get the income and expense amounts array

const expense_categories_amounts = JSON.parse(document.getElementById("expense_categories_amounts").innerHTML)
const income_categories_amounts = JSON.parse(document.getElementById("income_categories_amounts").innerHTML)


const data_expense = {
    labels: expense_categories_labels,
    datasets: [{
      label: 'Expenses by category',
      data: expense_categories_amounts,
      backgroundColor: [
        generate_random_color(),
        generate_random_color(),
        generate_random_color(),
        generate_random_color(),
        generate_random_color(),
        generate_random_color()
      ],
      hoverOffset: 4
    }]
  };