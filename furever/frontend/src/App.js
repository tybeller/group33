import './index.css';
import Header from './components/Header'
import About from './pages/About';
import Home from './pages/Home';
import Dogs from './pages/Dogs';

import { UserProvider } from "./contexts/user.context";
import Login from './pages/Login.page';
import PrivateRoute from './pages/PrivateRoute.page';
import Signup from './pages/Signup.page';
import Logout from './pages/Logout';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Profile from './pages/Profile';
import React from 'react'
import ReactDOM from 'react-dom'


function App() {
  return (
    
    <BrowserRouter> 
      <Header> 
        <UserProvider>
          <Routes>
            <Route exact path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} />
            <Route element={<PrivateRoute />}> 
              <Route path='/about' element={<About />} />
              <Route path='/home' element={<Home />} />
              <Route path='/dogs' element={<Dogs />} />
              <Route path='/profile' element={<Profile />} />
              <Route path='/logout' element={<Logout />} />
            </Route>
            
          </Routes>
        </UserProvider> 
      </Header>
    </BrowserRouter>
       
  );
}

export default App;