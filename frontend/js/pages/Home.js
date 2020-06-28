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

class Home extends Component {

    constructor(props) {
        super(props)        
        this.checkLocalStorage = this.checkLocalStorage.bind(this)
        this.setLocalStorage = this.setLocalStorage.bind(this)
        this.state = {loading: true}
    }

    checkLocalStorage(){
        if((window.localStorage.getItem('access_token')=="undefined" ||
         window.localStorage.getItem('access_token')==undefined) && 
         window.localStorage.getItem('user')=="undefined" || 
         window.localStorage.getItem('user')==undefined){
            return true
        }
        return false
    }

    setLocalStorage(){
        const url = this.props.location.search;
        const params = queryString.parse(url);
        
        if(this.checkLocalStorage()){ 
            trackPromise(
                axios.post('https://cors-anywhere.herokuapp.com/https://github.com/login/oauth/access_token',            
                    {
                        client_id: constants.client_id,
                        client_secret: constants.client_secret,
                        code: params.code
                    },
                    {headers : {Accept: 'application/json', 'Access-Control-Allow-Origin':'*'}},
                ).then(res => {     
                    if(res.data.error){
                        this.props.history.push("/login")
                    }
                    window.localStorage.setItem("access_token",res.data.access_token)
                    GithubApi.getUser().then(res => {
                       window.localStorage.setItem('user', res.login)                       
                       this.setState({loading: false})
                    }) 
                }).catch(res => console.log(res))
                )                          
        }
        else{
            this.setState({loading: false})
        }        
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