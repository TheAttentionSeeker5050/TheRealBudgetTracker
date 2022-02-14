import 'bootstrap/dist/css/bootstrap.css';

import React,  { useState } from "react";
import "../Static/Styles/filter_buttons.css"

export class ChangeDateButtons extends React.Component {
    constructor(props) {
        super(props);
        this.monthList = ["January","February","March","April","May","June","July",
        "August","September","October","November","December"];
        this.state = {
            currentMonth:this.props.month,
            currentYear:this.props.year,
        //   entryList: [],
        //   modal: false,
        //   startDate:"",
        //   endDate:"",
        //   activeItem: {
        //     title: "",
        //     description: "",
        //     completed: false,
        //   },
        };
      }

      renderNextMonthButton = (current_month, current_year) => {
          if (current_month != 12) {
            var next_month = current_month+1
            var next_year = current_year 
          } else {
            var next_month = 1
            var next_year = current_year+1
          }

          var month_list = this.monthList


          return (
              <button className='btn btn-primary'> {month_list[next_month-1]}-{next_year} >> </button>
          )
        
      }

      renderPreviousMonthButton = (current_month, current_year) => {
        if (current_month != 12) {
          var prev_month = current_month+1
          var prev_year = current_year 
        } else {
          var prev_month = 1
          var prev_year = current_year+1
        }

        var month_list = this.monthList


          return (
              <button className='btn btn-primary'> {month_list[prev_month-1]}-{prev_year} >> </button>
          )
      
    }

    render() {

        return (
            <div className='change_buttons'>
                {this.renderNextMonthButton(6, 2021)}
                {this.renderPreviousMonthButton(6, 2021)}
            </div>

        )
    }
    
}

// function ChangeDateButtons() {
//     // var [month, setMonth] = useState({})
//     // var [year, setYear] = useState({})
    
    
//     // let date = new Date()
        
//     // setMonth(date.getMonth)
//     // setYear(date.getFullYear)
    

//     return (
//         <div className="filter_div">
//             <h1>date</h1>
//             {/* <h1>{month}</h1>
//             <h1>{year}</h1> */}
//             {/* {console.log({year},"-",{month})} */}
//         </div>
    
//     )

    
    

// }

// export {ChangeDateButtons};