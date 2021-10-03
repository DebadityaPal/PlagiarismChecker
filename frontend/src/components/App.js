import '../styles/App.css';
import React from 'react';
import Image from '../assets/6316.jpg'

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <div className="App-home-card">
            <div class="typewriter">
              <h1>PLAGIO</h1>
            </div>
            <div className="subheading">
              We search your document against atleast <strong> 130 trillion webpages </strong> to provide you with the most comprehensive Plagiarism Check. 
            </div>
            <div className="check-button" onClick={(e) => this.props.history.push("/form")}>
              Check Now
            </div>
            <div className="made_by_container">
              Made with ❤️ by <strong><a href="https://github.com/DebadityaPal" target="_blank" title="Debaditya Pal" >@DebadityaPal</a></strong> 
            </div>
          </div>
          <div class="home_image_container">
            <img src={Image} alt="" />
          </div>
        </header>
      </div>
    );
  }
}

export default App;
