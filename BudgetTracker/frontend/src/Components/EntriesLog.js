import React, { Component } from "react";
import 'bootstrap/dist/css/bootstrap.css';
import "../Static/Styles/log.css"

// the api rest framework
import axios from "axios";

// we get or refresh list
const refreshList = () => {
  axios
    .get("/api/todos/")
    .then((res) => this.setState({ todoList: res.data }))
    .catch((err) => console.log(err));
};

const entry_list = []




function EntryItem(props) {
    return (
    <tr key="" className="log_table_item_row">
      <td scope="row">
        {props.entry_type}
      </td>
      <td >{props.description}</td>
      <td>{props.category}</td>
      <td>{props.date}</td>
      <td>${props.amount}</td>

    </tr>
)
}

function EntriesLog(props) {
    return (
        <div className="entries_log">
            <div className="table_div">
            <table class="table table-hover table-stripped">
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
                    {props.children}
                </tbody>
                </table>
            
            </div>
        </div>
    )
}

export  {EntriesLog, EntryItem};