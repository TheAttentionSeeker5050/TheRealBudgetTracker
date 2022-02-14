import React, { Component, useState } from "react";
import 'bootstrap/dist/css/bootstrap.css';
import "../Static/Styles/log.css";




function EntryItem(props) {
    return (
    <tr key="" className="log_table_item_row">
      <td>
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
                    {props.children}
                </tbody>
                </table>
            
            </div>
        </div>
    )
}

export  {EntriesLog, EntryItem};