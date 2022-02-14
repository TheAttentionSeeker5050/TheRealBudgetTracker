
// first we get month and year
function get_url_month_and_year() {
  const splited_url_string = window.location.pathname.split("/");
  const year =  splited_url_string[3]
  const month = splited_url_string[4]
  return [year, month]
}


const exp_year_month_array = get_url_month_and_year() // returns an array with position 0 as year and position 1 as month

// now we fetch data from our url

var url = `http://127.0.0.1:8000/api/entries/${exp_year_month_array[0]}/${exp_year_month_array[1]}/`


function get_from_api(url, callback) {
  // we fetch data from the API
  fetch(url)
    .then(response => response.json())
    .then(data => {
      obj = data
    })
    .then(() => callback(obj))
    .catch(err => console.log(err))
}


  
get_from_api(url, generate_chart)



function generate_chart(arr_of_objs) {
  // we process the data that we got from the apo into an expense chart


  labels = ["food", "housing", "transportation", "fun & entertainment", "investing", "interest & debts"],
  categories_sum_array = [0,0,0,0,0,0,0,0]

  // we categorize the expenses and sum them
  arr_of_objs.forEach((x) => {
    console.log(x)

    label_index = labels.indexOf(x.category)
    if (label_index != -1) {
      categories_sum_array[label_index] = categories_sum_array[label_index] + parseFloat(x.amount)
    }
  })

  // this is the json object that we will feed into our chart as data
  var data_expense = {
    labels:labels,  // ["Food", "Housing", "Transportation", "Fun & Entertainment", "Investing", "Interest & Debts"],
    datasets: [{
      label: 'Expenses by category',
      data: categories_sum_array,
      backgroundColor: [
        'rgba(255, 99, 132, 0.5)',
        'rgba(54, 162, 235, 0.5)',
        'rgba(255, 206, 86, 0.5)',
        'rgba(75, 192, 192, 0.5)',
        'rgba(153, 102, 255, 0.5)',
        'rgba(50, 201, 1, 0.5)',
        'rgba(240, 122, 223, 0.5)',
        'rgba(255, 159, 64, 0.5)'
      ],
      hoverOffset: 4
    }]
  };    

  // config file containing the chart type and the data json object
  const expense_config = {
    type: 'pie',
    data: data_expense,
  };

  // we build the expense chart and add the config file
  const myExpenseChart = new Chart(
    document.getElementById('expense_pie_chart'),
    expense_config
  );
}


    


