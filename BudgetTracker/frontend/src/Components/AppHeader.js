import logo from "../Static/Img/logo.png";
import "../Static/Styles/header.css";
import React, { Component } from "react";

function AppHeader() {
    return (
      <header className="app_header">
        <ul>
          <li>
            <img src={logo} alt="Company_logo" />            
          </li>
          <li> 
            <p>Add</p> 
          </li>
          <li> 
            <p>History</p> 
          </li>
          <li> 
            <p>Summary</p> 
          </li>
        </ul>
      </header>
    );
  }

export {AppHeader};