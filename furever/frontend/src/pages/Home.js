import '../index.css';
import DogSwipe from '../components/DogSwipe'
import { Button } from '@mui/material'
import { useContext } from 'react';
import { UserContext } from '../contexts/user.context';
function Home() {
  return(
  <div className="App bg-red-300">
    <header classname="App-header">
        <DogSwipe/>
    </header>
  </div>
  );
}

export default Home;