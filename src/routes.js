import React from 'react';
import { Route, IndexRoute, Redirect } from 'react-router';
import App from './components/App';
// import CounterApp from './containers/CounterApp';
import GymlogApp from './containers/GymlogApp';


export default (
  <Route path="/" component={App}>
    <IndexRoute component={GymlogApp}/>
    <Redirect from="*" to="/"/>
  </Route>
);
