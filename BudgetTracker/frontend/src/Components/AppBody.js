import React,  { useState } from "react";

import {EntriesLog, EntryItem} from './EntriesLog';
import {ChangeDateButtons} from "./ChangeDateButtons";

import "../Static/Styles/log.css";

// the api rest framework
import axios from "axios";

class AppBody extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      entryList: [],
      modal: false,
      startDate:"",
      endDate:"",
      activeItem: {
        title: "",
        description: "",
        completed: false,
      },
    };
    // this.date= new Date()
  }

// const entry_list = []

  // we set this in order to render the component 
  componentDidMount() {
    this.getDates(2021,6);
    console.log("got dates")
    this.refreshList();
    console.log("refreshed list")
    console.log("rendering list")
  }

  

  // componentNeedsUpdate



  refreshList = () => {

    axios
    .get("/api/entries/")
    .then((res) => { 
      this.setState({entryList: res.data})
    })
    .catch((err) => console.log(err));
  }

  getDates(year=null, month=null) {
    if (!month && !year) {

      const now = new Date()
      var now_month = now.getMonth()
      var now_year = now.getFullYear()
      var next_month_date

    } else {
      // if there are parameters in this function
      var now_month = month
      var now_year = year
      var next_month_date


    }

    // this is the logic for next month
    if (now_month == 11) {
      next_month_date = new Date(now_year + 1, 0, 1);
    } else {
      next_month_date = new Date(now_year, now_month + 1, 1);
    }
    var next_month_month = next_month_date.getMonth()
    var next_month_year = next_month_date.getFullYear()
    
    // we put a 0 in front of the month number just to make sure the filter fits
    if (now_month >= 9){
      this.setState({startDate:`${now_year}-${now_month+1}-01`})
    } else {
      this.setState({startDate:`${now_year}-0${now_month+1}-01`})
    }

    // we put a 0 in front of the month number just to make sure the filter fits
    if (next_month_month>=9) {
      this.setState({endDate:`${next_month_year}-${next_month_month+1}-01`})
    } else {
      this.setState({endDate:`${next_month_year}-0${next_month_month+1}-01`})

    }
  }
  
  renderItems = () => {
    // we have the dates
    const start_date = this.state.startDate //  `2021-00-1`// 
    const end_date = this.state.endDate // `2022-01-1` // this.state.endDate //


    console.log(this.state.startDate)

    console.log(this.state.endDate)

    const filteredList = this.state.entryList.filter(function (list) {
      // console.log(list.date >= start_date  && list.date < end_date)
      console.log(start_date)
      return list.date >= start_date  && list.date < end_date
    })

    console.log(filteredList)
    console.log("after filter")
    
    


    return filteredList.map(
      (entry) => (
        
        <tr className="log_table_item_row">
          <td>
            {entry.entry_type}
          </td>
          <td >{entry.description}</td>
          <td>{entry.category}</td>
          <td>{entry.date}</td>
          <td>${entry.amount}</td>

        </tr>
    )
  )
  }


  render() {
    
    //  we pass the component props 
    const month = this.state.startDate.slice(4, 6)
    const year = this.state.startDate.slice(0, 4)


    return (
    <div className="app_body">
      
      
      
      <div className="table_div">
            <table className="table table-hover table-stripped">
                <thead>
                    <tr className="log_table_item_head">
                        <th scope="col">Entry type</th>
                        <th scope="col">Description</th>
                        <th scope="col">Category</th>
                        <th scope="col">Date</th>
                        <th scope="col">Amount</th>
                    </tr>
                </thead>
                <tbody>
                    
                  {this.renderItems()}
                </tbody>
                </table>
            
            </div>
    
    

    <ChangeDateButtons
      month={month}
      year={year}
    />
    </div>
    )
  }



}

export {AppBody};