import React from 'react';
import { createRoot } from 'react-dom/client';
import '../../styles/sass/styles.scss';

import FilterApp from './FilterComponent/FilterApp';

let myFilterApp = document.getElementById('myFilterApp');

if (myFilterApp) {
      const root = createRoot(myFilterApp);
    root.render(<FilterApp />);
}
