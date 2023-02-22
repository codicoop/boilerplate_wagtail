import React from 'react';
import { createRoot } from 'react-dom/client';
import '../../styles/sass/styles.scss';

import FilterApp from './FilterComponent/FilterApp';
import SliderApp from './SliderComponent/SliderApp';
import HistoryApp from './HistoryComponent/HistoryApp';

// Aplicació que filtra models i els mostra
let myFilterApp = document.getElementById('myFilterApp');

if (myFilterApp) {
      const root = createRoot(myFilterApp);
    root.render(<FilterApp />);
}

// Aplicació que gestiona el slider de "Qui som"
let mySliderApp = document.getElementById('mySliderApp');

if (mySliderApp) {
      const root = createRoot(mySliderApp);
    root.render(<SliderApp />);
}

// Aplicació que gestiona l'apartat història de "Qui som"
let myHistoryApp = document.getElementById('myHistoryApp');

if (myHistoryApp) {
      const root = createRoot(myHistoryApp);
    root.render(<HistoryApp />);
}
