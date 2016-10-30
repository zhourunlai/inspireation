/**
 * Created by pie on 2016-10-30.
 */
import React, {Component} from 'react';
import cs from 'classnames';
export default class AccountBar extends  Component{
    static defaultProps = {
        theme: 'blue'
    };

    render(){
        const theme = Boolean(this.props.theme == 'blue');

        let accountClass = cs('account',{'account-blue':theme},{'account-org':!theme});
        return (
            <span className={accountClass}><span className="register">注册</span> / <span className="login">登录</span></span>
        )
    }
}