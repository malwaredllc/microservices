import React from 'react';
import logo from './logo.svg';
import './App.css';
import Nav from './components/Nav/Nav';
import Menu from './components/Menu/Menu';
import Products from './admin/Products';
import Main from './main/Main';
import {BrowserRouter, Route} from 'react-router-dom';

function App() {
  return (
    <div className="App">    
          <main role="main" className="col-md-9 ms-sm-auto col-lg-10 px-md-4">

            <BrowserRouter>
              <Route path='/admin/products' component={Products}></Route>
              <Route path='/' component={Main}></Route>
              
            </BrowserRouter>
          </main>
    </div>
  );
}

export default App;
