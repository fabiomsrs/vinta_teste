import React, { Component } from 'react'
import { connect } from 'react-redux';
import axios from 'axios';

import { trackPromise } from 'react-promise-tracker';
import IconButton from '@material-ui/core/IconButton';
import DeleteIcon from '@material-ui/icons/Delete';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import ApiService from '../../../utils/service/ApiService'
import LoadingIndicator from '../Loader'


class RepoTable extends Component {

    constructor(props) {
        super(props) 
        this.state = {
            repos: [],
        };
    }

    delete(id, e){              
        const { repos } = this.state
        const reposUpdated = repos.filter(repo => {            
            return repo.id !== id
        })         
        trackPromise(ApiService.deleteRepo(id))
        this.setState({repos: reposUpdated})
    }
    componentDidUpdate(prevProps){
        if(this.props.repos !== prevProps.repos){
            this.setState({
                repos: [this.props.repos.pop(), ...this.state.repos]
            })
        }
    }

    componentDidMount(){
        trackPromise(
            ApiService.listRepo().then(res => {                            
                if (res) {
                    this.setState({
                        repos: [...res]
                    })                
                }
            }).catch(err => console.log(err))
            )   
    }

    render() {             
            return (  
                <>
                    <TableContainer>
                    <Table aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell>Repositório</TableCell>
                                <TableCell align="right">Usuário</TableCell>
                                <TableCell align="right">Data/Hora</TableCell>
                                <TableCell align="right"></TableCell>                            
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {this.state.repos.map((repo) => (
                                <TableRow key={repo.id}>
                                    <TableCell component="th" scope="row">
                                        {repo.name}
                                    </TableCell>
                                    <TableCell align="right">{repo.owner}</TableCell>
                                    <TableCell align="right">{repo.date}</TableCell>                                
                                    <TableCell size="small" align="center">
                                        <IconButton color="secondary" aria-label="add a search" onClick={this.delete.bind(this,repo.id)}>
                                            <DeleteIcon/>
                                        </IconButton> 
                                    </TableCell>                                
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
                <LoadingIndicator/>
            </>          
        )
    }
}

const mapStateToProps = state => ({
    repos: state.repos
})

export default connect(mapStateToProps)(RepoTable);