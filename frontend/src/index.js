import React from "react";
import ReactDOM from "react-dom";
// import "./scss/app.scss";
import App from "./App";
import { BrowserRouter as Router } from "react-router-dom";
// import store from './redux/store';
// import { Provider } from 'react-redux';

// import "./style.scss";
import "./styles/style.scss";

ReactDOM.render(
    <React.StrictMode>
        <Router>
            {/* <Provider store={store}> */}
            <App />
            {/* </Provider> */}
        </Router>
    </React.StrictMode>,
    document.getElementById("app")
);