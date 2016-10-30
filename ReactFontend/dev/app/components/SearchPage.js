/**
 * Created by pie on 2016-10-30.
 */
import React, {Component} from 'react';
import TopBar from './TopBar';
import VoiceInput from './VoiceInput';


export default class SearchPage extends Component{

    render(){
        const searchTitlePath = require('images/search/search_title.png');
        return(
            <div className="page">
                <TopBar theme="org"/>
                <img className="search-title" src={searchTitlePath}/>
                <VoiceInput/>
            </div>
        )
    }
}