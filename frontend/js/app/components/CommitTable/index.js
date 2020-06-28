import React, { Component, Fragment } from 'react'
import { Link } from 'react-router-dom';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import { Pagination } from '@material-ui/lab';
import { trackPromise } from 'react-promise-tracker';
import LoadingIndicator from '../Loader'

class CommitTable extends Component {

    constructor(props) {
        super(props)
        this.state = {
            commit: [],
            page: 1,
            total_pages: 1,
            commit_function: this.props.commit_function,
            repo: this.props.repo
        };
    }

    handleChange(event, page){
        let commit_function
        if(this.state.repo){
            commit_function = this.state.commit_function(this.state.commit[0].repo.id, page)
        }else{
            commit_function =this.state.commit_function(page)
        }
        trackPromise(
            commit_function.then(res => {
                if (res.results) {                
                    this.setState({
                        commit: [...res.results],
                        page: res.page,
                        total_pages: res.total_pages,
                    })
                }
            }).catch(err => console.log(err))
        )
    }    

    componentDidMount() {
        let commit_function
        if(this.state.repo){
            commit_function = this.state.commit_function(this.state.repo)
        }else{
            commit_function =this.state.commit_function()
        }
        trackPromise(
            commit_function.then(res => {
                if (res.results) {                       
                    this.setState({
                        commit: [...res.results],
                        page: res.page,
                        total_pages: res.total_pages,
                        repo_page: true
                    })
                }
            }).catch(err => console.log(err))
        )
    }

    render() {
        return (
            <Fragment>
            <TableContainer>
                <Table aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell>Commit</TableCell>
                            <TableCell>Autor</TableCell>
                            <TableCell align="right">Repositório</TableCell>
                            <TableCell align="right">Data/Hora</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {this.state.commit.map((commit) => (
                            <TableRow key={commit.id}>
                                <TableCell>{commit.id}</TableCell>
                                <TableCell component="th" scope="row">
                                    {commit.author}
                                </TableCell>
                                <TableCell align="right">
                                    <Link id={commit.repo.id} to={"/repo/"+commit.repo.id+"/commit"}>
                                        {commit.repo.name}
                                    </Link>
                                </TableCell>
                                <TableCell align="right">{commit.date}</TableCell>                                
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
            <Pagination count={this.state.total_pages} page={this.state.page} color='primary' onChange={this.handleChange.bind(this)}/>
            <LoadingIndicator/>
          </Fragment>
        )
    }
}

export default CommitTable;