import '../styles/App.css';
import React from 'react';

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
              We search your document against atleast 130 trillion webpages to provide you with the most comprehensive Plagiarism Check. 
            </div>
            <div className="check-button" onClick={(e) => this.props.history.push("/form")}>
              Check Now
            </div>
          </div>
        </header>
      </div>
    );
  }
}

export default App;
