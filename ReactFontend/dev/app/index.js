import React from 'react';
import {render} from 'react-dom';
import { Router, Route, hashHistory } from 'react-router';
import App from './components/App';
import SearchPage from './components/SearchPage';


// const attachFastClick = require('fastclick');
// attachFastClick(document.body);

render(
    <Router history={hashHistory}>
        <Route path='/' component={App}/>
        <Route path='/search' component={SearchPage}/>
    </Router>,
    document.querySelector('#app-container')
);
