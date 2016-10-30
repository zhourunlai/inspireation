/**
 * Created by pie on 2016-10-30.
 */
import React, {Component, PropTypes} from 'react';
export  default class VoiceInput extends  Component{
    render(){
        return (
            <div className="voice-input-container">
                <input type="text" className="search-input" placeholder="输入文字或段落"/>
                <img src={require('images/search/voice_icon.png')} className="voice-icon"/>
                <img src={require('images/search/search_icon.png')} className="search-icon"/>
            </div>
        )
    }
}