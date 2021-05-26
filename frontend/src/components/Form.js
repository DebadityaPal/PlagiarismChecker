import '../styles/App.css';
import '../styles/Form.css'
import React from 'react';

class Form extends React.Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <button type="button" class="btn btn-primary back-button" onClick={(e) => this.props.history.push("/")}>Back to Home Page</button>
          <div className="Form-card">
            <div className="Form-name">PLAGAWARE</div>
            <form>
              <div className="Form-heading">Choose your input</div>
              <div className="Form-choice">
                <div>
                  <input type="radio" name="choice" id="choice-text" required />
                  <label for="choice-text" style={{paddingLeft:"10px"}}>Text</label>
                </div>
                <div>
                  <input type="radio" name="choice" id="choice-file" required />
                  <label for="choice-file" style={{paddingLeft:"10px"}}>Upload Text or Doc</label>
                </div>
                <div>  
                  <input type="radio" name="choice" id="choice-ocr" required />
                  <label for="choice-ocr" style={{paddingLeft:"10px"}}>Upload Image (OCR)</label>
                </div>
              </div>
            </form>
          </div>
        </header>
      </div>
    );
  }
}

export default Form;
