import React, { Component, Fragment} from 'react'
import { Container } from '@material-ui/core';
import Paper from '@material-ui/core/Paper';
import Header from '../app/components/Header'
import CommitTable from "../app/components/CommitTable"
import ApiService from '../utils/service/ApiService'


class Commit extends Component {

    constructor(props) {
        super(props)
    }

    componentDidMount() {        
        
    }

    render() {
        return (
            <Fragment>
                <Header />
                <Container component={Paper} maxWidth="lg">                    
                    <CommitTable commit_function={ApiService.listCommit}/>
                </Container>
            </Fragment>
        )
    }
}

export default Commit