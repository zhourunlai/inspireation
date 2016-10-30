/**
 * Created by pie on 2016-10-29.
 */
import React, {Component, PropTypes} from 'react';
import AccountBar from './AccountBar';
import cs from 'classnames';

export default class HalfWrap extends Component {
    static propTypes = {
        direction: PropTypes.string.isRequired
    };

    render() {
        const direction = this.props.direction;

        const titlePath = require('images/wrap/title_' + direction + '.png');
        const iconPath = require('images/wrap/icon_'+ direction + '.png');
        const logoPath = require('images/logo_blue.png');
        const antiDirection = (direction == 'left') ? 'right' : 'left';
        let topBody;
        if (direction == 'left'){
            topBody = <img src={logoPath}/>;
        }else {
            topBody= <AccountBar/>;
        }
        return (
            <div className={cs('wrap', direction, 'wrap-' + direction)}>
                <div className={cs('top-box',direction)}>{topBody}</div>
                <div className={cs('rect-container', antiDirection, 'rect-' + direction)}>
                    <div className={cs('circle', antiDirection,'circle-'+direction)}/>
                    <img className={cs('rect-title', antiDirection)} src={titlePath}/>
                </div>
                <img className='wrap-bottom-icon' src={iconPath}/>
            </div>
        )
    }
}