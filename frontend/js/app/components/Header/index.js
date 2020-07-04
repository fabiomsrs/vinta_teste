import React from 'react';
import { Link } from 'react-router-dom';
import { useHistory } from "react-router-dom";
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    marginBottom: theme.spacing(2)
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

export default function ButtonAppBar() {
  const classes = useStyles();
  let history = useHistory()

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>          
          <Typography variant="h6" className={classes.title}>
            <Link to="/home" style={{color:'#FFF'}}>
              Github Monitor
            </Link>
          </Typography>
          <Link to="/home" style={{color:'#FFF'}}>
            <Button color="inherit">Home</Button>
          </Link>
          <Link to="/commit" style={{color:'#FFF'}}>
            <Button color="inherit">Commits</Button>
          </Link>
          <Link onClick={() => {window.localStorage.clear(), history.push('/login')}} to="#" style={{color:'#FFF'}}>
            <Button color="inherit">Logout</Button>
          </Link>
        </Toolbar>
      </AppBar>
    </div>
  );
}
