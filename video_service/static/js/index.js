import React from 'react';
import ReactDOM from 'react-dom';
import Name from './name';
import '../css/hello.css';


const counter = document.getElementById('counter');
let count = 0;

setInterval(() => counter.innerText = ++count, 1000);


ReactDOM.render(<Name />, document.getElementById('name'));
