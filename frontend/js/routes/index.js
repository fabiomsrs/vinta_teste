import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom'

import Commit from '../pages/Commit';
import RepoCommit from '../pages/RepoCommit';
import Home from '../pages/Home';
import Login from '../pages/Login';

const Router = () => (
    <BrowserRouter>
        <Switch>
        <Route path='/login' exact={true} component={Login} />
        <Route path='/logout' exact={true} component={Login} />
        <Route path='/home' exact={true} component={Home} />        
        <Route path='/commit' exact={true} component={Commit} />        
        <Route path='/repo/:id/commit' exact={true} component={RepoCommit} />        
        </Switch>
    </BrowserRouter>
);

export default Router;