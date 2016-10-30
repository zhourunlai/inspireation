/**
 * Created by pie on 2016-10-30.
 */
import React, {Component} from 'react';
import AccountBar from './AccountBar';
import {Row, Col} from 'antd';

export default class TopBar extends Component {
    static defaultProps = {
        theme: 'blue'
    };

    render() {
        const theme = this.props.theme;
        const logoPath = require('images/logo_' + theme + '.png');
        let tabBody;
        if (theme == 'blue') {
            tabBody = <div className="taps">
                <div className="tap current-tap">Inspiration</div>
                <div className="tap current-tap-red">Creation</div>
            </div>
        } else {
            tabBody = <div className="taps">
                <div className="tap ">Inspiration</div>
                <div className="tap current-tap-red">Creation</div>
            </div>
        }
        return (
            <div>
                <Row>
                    <Col span={4}>
                        <img className="logo" src={logoPath}/>
                    </Col>
                    <Col span={6}>
                        <div className="taps">
                            <div className="tap ">Inspiration</div>
                            <div className="tap current-tap-red">Creation</div>
                        </div>
                    </Col>
                    <Col span={8} offset={6}>
                        <div className="account"><AccountBar theme={theme}/></div>
                    </Col>
                </Row>
            </div>
        )
    }
}