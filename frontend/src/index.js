import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route} from "react-router-dom";
import './index.css';
import App from './components/App';
import Form from './components/Form';

const Routing = () => {
  return(
    <Router>
      <Switch>
        <Route exact path="/" component={App} />
        <Route exact path="/form" component={Form} />
      </Switch>
    </Router>
  )
}

ReactDOM.render(
  <React.StrictMode>
    <Routing />
  </React.StrictMode>,
  document.getElementById('root')
)