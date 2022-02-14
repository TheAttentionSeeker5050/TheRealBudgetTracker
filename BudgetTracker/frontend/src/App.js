import logo from './logo.svg';
import './App.css';

import "./Static/Styles/app.css"

import React, { Component } from "react";
import { AppHeader } from './Components/AppHeader';
import {AppBody} from './Components/AppBody';





function App() {
  return (
    <div className="App">
      <AppHeader/>
      <AppBody/>
    </div>
  );
}

export default App;
