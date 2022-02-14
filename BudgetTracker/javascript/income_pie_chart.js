
// first we get month and year
function get_url_month_and_year() {
    const splited_url_string = window.location.pathname.split("/");
    
    const year =  splited_url_string[3]
    const month = splited_url_string[4]
    return [year, month]
  }
  
  
  const year_month_array = get_url_month_and_year() // returns an array with position 0 as year and position 1 as month
  
  // now we fetch data from our url
  
  var url = `http://127.0.0.1:8000/api/entries/${year_month_array[0]}/${year_month_array[1]}/`
 
  
  function get_from_api(url, callback) {
    // we fetch data from the API
    fetch(url)
      .then(response => response.json())
      .then(data => {
        obj = data
        console.log(obj)
      })
      .then(() => callback(obj))
      .catch(err => console.log(err))
  }
  
  
    
  get_from_api(url, generate_chart)
  
  
  
  function generate_chart(arr_of_objs) {
    // we process the data that we got from the apo into an expense chart
  
  
    labels = ["allowance", "work", "investment returns"],
    categories_sum_array = [0,0,0]
  
    // we categorize the expenses and sum them
    arr_of_objs.forEach((x) => {  
      label_index = labels.indexOf(x.category)
      if (label_index != -1) {
        categories_sum_array[label_index] = categories_sum_array[label_index] + parseFloat(x.amount)
      }
    })
  
    // this is the json object that we will feed into our chart as data
    var data_income = {
      labels:labels,  // ["Food", "Housing", "Transportation", "Fun & Entertainment", "Investing", "Interest & Debts"],
      datasets: [{
        label: 'Income by category',
        data: categories_sum_array,
        backgroundColor: [
          'rgba(153, 232, 142, 1)',
          'rgba(210, 4, 226, 1)',
          'rgba(55, 28, 250, 1)'
          
        ],
        hoverOffset: 4
      }]
    };    
  
    // config file containing the chart type and the data json object
    const income_config = {
      type: 'pie',
      data: data_income,
    };
  
    // we build the expense chart and add the config file
    const myIncomeChart = new Chart(
      document.getElementById('income_pie_chart'),
      income_config
    );
  }
  
  
      
  