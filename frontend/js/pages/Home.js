import React, { Component, Fragment} from 'react'
import { Container } from '@material-ui/core';
import queryString from 'query-string';
import { trackPromise } from 'react-promise-tracker';
import constants from "../constants/gitcredentials"
import Header from '../app/components/Header'
import RepoForm from '../app/components/RepoForm'
import RepoTable from "../app/components/RepoTable"
import GithubApi from "../utils/service/GithubService"
import LoadingIndicator from '../app/components/Loader'
import axios from 'axios';
import ApiService from '../utils/service/ApiService';

class Home extends Component {

    constructor(props) {
        super(props)             
        this.setLocalStorage = this.setLocalStorage.bind(this)
        this.state = {loading: true}
    }    

    setLocalStorage(){                
        trackPromise(
            ApiService.getUser().then(res=>{        
                window.localStorage.setItem('csrf',res.extra_data.csrf)
                window.localStorage.setItem('user', res.extra_data.login)
                window.localStorage.setItem("access_token",res.extra_data.access_token)           
                this.setState({loading: false})
            }).catch(err => { 
                this.props.history.push("/login")
            })            
        )                                          
    }

    componentDidMount() { 
        this.setLocalStorage()
    }

    render() {        
        return (
            <Fragment>
                <Header />
                <Container maxWidth="lg">                
                {
                this.state.loading ? 
                    <LoadingIndicator/>              
                    :
                    <>
                        <RepoForm/>
                        <RepoTable/>                        
                    </>
                }                
                </Container>
            </Fragment>
        )
    }
}

export default Home