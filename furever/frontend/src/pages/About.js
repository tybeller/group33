import '../index.css';
import '../App.css';

import AboutPage from '../components/AboutPage.js'
function About() {
  return(
  <div className="App bg-blue-50">
    <header classname="App-header">
      <div classname="aboutpage">
          <AboutPage/>
      </div>
    </header>
  </div>
  );
}

export default About;