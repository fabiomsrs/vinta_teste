import React, { Component } from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { trackPromise } from 'react-promise-tracker';

import IconButton from '@material-ui/core/IconButton';
import AddIcon from '@material-ui/icons/Add';
import { Button } from '@material-ui/core';
import { TextField } from '@material-ui/core';
import { FormControl } from '@material-ui/core';
import { FormGroup } from '@material-ui/core';


import * as reposActions from '../../../actions/repo'
import GithubService from '../../../utils/service/GithubService'
import ApiService from '../../../utils/service/ApiService'
import FormValidator from '../../../utils/FormValidator'
import Toast from '../Toast'



class RepoForm extends Component {

    constructor(props) {
        super(props)        
        this.validator = new FormValidator([
            {
                field:'user',
                method:'isEmpty',                
                message: 'Campo usuário vazio'
            },
            {
                field:'repo',
                method:'isEmpty',             
                message: 'Campo repositório vazio'
            }
        ]);
        this.initState = {
            user: '',
            repo: '',
            validation: this.validator.valid(),
            message: {
                open: false,
                text: '',
                type: ''
            }
        }
        this.state = this.initState
    }

    inputListener(event) {        
        const { name, value } = event.target
                
        this.setState({
            [name]: value
        })
    }

    submit() {   
        const validation = this.validator.validate(this.state)        
        if(validation.isValid){                  
            trackPromise( 
                GithubService.getRepo(this.state.user, this.state.repo).then(async res => {
                    await ApiService.createRepo(res).then(res => {
                        this.props.addRepo(res)                                         
                        this.setState({
                            message: {
                                messages: "Repositósio salvo",
                                type: 'success',
                                open: true
                            }
                        })
                    }).catch(err => {
                       err = JSON.parse(err.message)                       
                       this.setState({
                            message: {
                                messages: err.non_field_errors.pop(),
                                type: 'error',
                                open: true
                            }
                        })
                    }) 
            }).catch(err => {                
                this.setState({
                    message: {
                        messages: "Repositósio não encontrado",
                        type: 'error',
                        open: true
                    }
                })                
            }));
            this.setState(this.initState)
        }else{                        
            const {user, repo} = validation;
            const fields = [user, repo];

            const invalidFields = fields.filter(elem => {
                return elem.isInvalid;
            });
            const errors = invalidFields.reduce(
                (errors, field) =>errors + field.message + '. ',
                ''
            )
            this.setState({
                message: {
                    messages: errors,
                    type: 'error',
                    open: true
                }
            })
        }
    }    

    render() {    
            
        const { user, repo } = this.state
        return (
        <>
            <Toast
                    open={this.state.message.open}
                    handleClose={() =>
                        this.setState({ message: { open: false } })
                    }
                    severity={this.state.message.type}
                >
                    {this.state.message.messages}
            </Toast>
            <FormControl fullWidth={true}>
                <FormGroup row={true}>
                    {/* <InputLabel htmlFor="user">Usuário</InputLabel> */}
                    <TextField id="user" name="user" margin="dense" label="Usuário" value={user} onChange={this.inputListener.bind(this)} variant="outlined" />
                    {/* <InputLabel htmlFor="repo">Repositório</InputLabel> */}
                    <TextField id="repo" name="repo" margin="dense" label="Repositório" value={repo} onChange={this.inputListener.bind(this)} variant="outlined" />
                    <IconButton color="secondary" aria-label="add a search" onClick={this.submit.bind(this)}>
                        <AddIcon/>
                    </IconButton>                    
                </FormGroup>
            </FormControl> 
        </>
        )
    }
}

const mapDispatchToProps = dispatch => bindActionCreators(reposActions, dispatch)

export default connect(null, mapDispatchToProps)(RepoForm);

