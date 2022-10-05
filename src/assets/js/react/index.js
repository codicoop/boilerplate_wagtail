import React from 'react';
import ReactDOM from "react-dom";

import FilterApp from './FilterComponent/FilterApp';

let myFilterApp = document.getElementById('myFilterApp');

if (myFilterApp) {
  ReactDOM.render(<FilterApp />, myFilterApp);
}
