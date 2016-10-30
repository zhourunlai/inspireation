/**
 * Created by piepieliu on 2016/8/30.
 */
import cs from 'classnames';
import React, {Component, PropTypes} from 'react';
import HalfWrap from './HalfWrap';
import 'less/app.less';


export default class App extends Component {
    render() {
        return (
            <div id="wrap-container">
                <HalfWrap direction="left"/>
                <HalfWrap direction="right"/>
            </div>
        )
    }
}