import './index.css';
import Header from './components/Header'
import About from './pages/About';
import Home from './pages/Home';
import Users from './pages/Users';
import Dogs from './pages/Dogs';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Profile from './pages/Profile';

function App() {
  return (
    
    <BrowserRouter> 
        <Header>
          <Routes>
            <Route path='/about' element={<About />} />
            <Route path='/home' element={<Home />} />
            <Route path='/users' element={<Users />} />
            <Route path='/dogs' element={<Dogs />} />
            <Route path='/profile' element={<Profile />} />
          </Routes>
            
        </Header>
    </BrowserRouter>
       
  );
}

export default App;