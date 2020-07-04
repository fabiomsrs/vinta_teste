import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Container } from '@material-ui/core'
import { Button } from '@material-ui/core';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import constants from '../constants/gitcredentials'
import GitHubIcon from '@material-ui/icons/GitHub';
import { Urls } from '../utils'

const useStyles = makeStyles((theme) => ({
    root: {
        marginTop: theme.spacing(8),        
        maxWidth: 345,
    },
    media: {
        height: 0,
        paddingTop: '56.25%', // 16:9
    },    
    icon: {        
        width: 345,
        height: '10em',
    }
}));

export default function Login() {
    const classes = useStyles();    
    return (
        <Container maxWidth='xs'>
            <Card className={classes.root}>
                <CardHeader
                    title="Github Monitor"
                    style={{'textAlign':'center'}}
                    />
                {/* <CardMedia
                    
                    title="Paella dish"
                    /> */}
                    <GitHubIcon className={classes.icon}/>
                <CardContent>
                <Button fullWidth={true} variant="contained" color="primary" href={Urls['social:begin']('github')}>
                    Sign in
                </Button>
                </CardContent>
            </Card>
        </Container>
    );
}

