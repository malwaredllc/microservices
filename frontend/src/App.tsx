import React from 'react';
import logo from './logo.svg';
import './App.css';
import Products from './admin/Products';
import Main from './main/Main';
import {BrowserRouter, Route} from 'react-router-dom';

function App() {
  return (
    <div className="App">    
          <main role="main" className="col-md-9 ms-sm-auto col-lg-10 px-md-4">

            <BrowserRouter>
              <Route path='/' exact component={Main}></Route>
              <Route path='/admin/products' component={Products}></Route>
              
            </BrowserRouter>
          </main>
    </div>
  );
}

export default App;
