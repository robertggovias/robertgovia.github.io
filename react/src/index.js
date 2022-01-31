import { render } from '@testing-library/react';
import react from 'react';
import React from 'react';
import reactDom from 'react-dom';
import './index.css';
//import reportWebVitals from './reportWebVitals';

/*
ReactDOM.render(
  <h1>Hello, React!</h1>,
  document.getElementById('root')
);*/

//Expressions in JSX
/*
const name = "Pepe";
const surname = "Canija";
const el = <p>Hello, {name} {surname}</p>;

ReactDOM.render(
  el,
  document.getElementById('root')
);
*/
/*
let counter = 0;

function show() {
  counter++;
  const el = <p>world population men {counter}, women {counter*2}</p>;
  ReactDOM.render(
    el, document.getElementById('root')
  );
}

setInterval(show, 1); 
*/

// Functional Components
/*
function Hello() {
  return <h1>Hello world.</h1>;
}

const el = <Hello/>;
reactDom.render(
  el,
  document.getElementById('root')
);
*/

//Class components
/*const nameP = "Pepe class component"
class Hello extends React.Component {
  render() {
    return <h2>Hello {nameP}</h2>;
  }
}
const el = <Hello />;
reactDom.render(
  el,
  document.getElementById('root')
);*/

// Props

function Item(props) {
  return <div className="item">
    <b>Name:</b> {props.name} <br />
    <b>Price:</b> {props.price}    
    </div>;
}

function App() {
  return <div>
    <Item name="Oro" price ="45"/>
    <Item name= "Plata" price = "53"/>
    <Item name= "Mirra" price = "34"/>
  </div>;
}

const el = <App />;
reactDom.render(
  el,
  document.getElementById('root') 
)

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
//reportWebVitals();
