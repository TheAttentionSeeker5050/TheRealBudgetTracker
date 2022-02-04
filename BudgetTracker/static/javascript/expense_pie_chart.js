// first we import our random color generator

function generate_random_color() {
    // we generate a random color
    let maxVal = 0xFFFFFF; // 16777215
    let randomNumber = Math.random() * maxVal; 
    randomNumber = Math.floor(randomNumber);
    randomNumber = randomNumber.toString(16);
    let randColor = randomNumber.padStart(6, 0); 
    return randColor  
}

function replace_quotes(string) {
    str = string.replace(/'/g, '"')
    return str
}


console.log(typeof(document.getElementById("expense_categories_labels").innerHTML))

// we get the income and expense label array
const expense_categories_labels_string = replace_quotes(document.getElementById("expense_categories_labels").innerHTML)
console.log(expense_categories_labels_string)
console.log(typeof(expense_categories_labels_string))
const expense_categories_labels = JSON.parse(expense_categories_labels_string)





// console.log(expense_categories_labels)
// JSON.parse(document.getElementById("expense_categories_labels").innerHTML)

const income_categories_labels = JSON.parse(document.getElementById("income_categories_labels").innerHTML)

// we get the income and expense amounts array

const expense_categories_amounts = JSON.parse(document.getElementById("expense_categories_amounts").innerHTML)
const income_categories_amounts = JSON.parse(document.getElementById("income_categories_amounts").innerHTML)

console.log(expense_categories_amounts)
console.log(generate_random_color())

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

    
const expense_config = {
    type: 'pie',
    data: data_expense,
    };    

const myExpenseChart = new Chart(
    document.getElementById('expense_pie_chart'),
    expense_config
  );