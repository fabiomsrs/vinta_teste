import React from 'react';
import { Provider } from 'react-redux';
import { hot } from 'react-hot-loader/root';

import SentryBoundary from './utils/SentryBoundary';
import Router from './routes'
import store from './store';


const App = () => (
  <SentryBoundary>
    <Provider store={store}>
      <Router />
    </Provider>
  </SentryBoundary>
);

export default hot(App);
