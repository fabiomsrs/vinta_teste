import React, { Component, Fragment} from 'react'
import { Container } from '@material-ui/core';
import Header from '../app/components/Header'
import CommitTable from "../app/components/CommitTable"
import ApiService from '../utils/service/ApiService'


class RepoCommit extends Component {

    constructor(props) {
        super(props)
    }

    componentDidMount() {                
    }

    render() {
        return (
            <Fragment>
                <Header />
                <Container maxWidth="lg">                    
                    <CommitTable commit_function={ApiService.listRepoCommits} repo={this.props.match.params.id}/>
                </Container>
            </Fragment>
        )
    }
}

export default RepoCommit