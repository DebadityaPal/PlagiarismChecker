import '../styles/App.css';
import '../styles/Form.scss'
import { FileUpload } from "primereact/fileupload"
import 'primereact/resources/themes/saga-green/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';
import React from 'react';

class Form extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      radio: "text"
    };
    this.handleRadioChange = this.handleRadioChange.bind(this);
    this.handleFileUpload = this.handleFileUpload.bind(this);
    this.handleTextarea = this.handleTextarea.bind(this);
    this.handleTextSubmit = this.handleTextSubmit.bind(this);
  }

  handleRadioChange(event) {
    this.setState({
      radio: event.target.value
    });
  }

  handleFileUpload(event) {
    this.setState({ selectedFile: event.target.files[0]});
  }

  handleTextarea(event) {
    this.setState({ text: event.target.value})
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <button type="button" class="btn btn-primary back-button" onClick={(e) => this.props.history.push("/")}>Back to Home Page</button>
          <div className="Form-card">
            <div className="Form-name">PLAGAWARE</div>
            <form onSubmit={this.handleSubmit}>
              <div className="Form-heading">Choose your input</div>
              <div className="Form-choice">
                <div>
                  <input type="radio" name="choice" id="choice-text" value="text" onChange={e => this.handleRadioChange(e)} required />
                  <label for="choice-text" style={{paddingLeft:"10px"}}>Text</label>
                  <div class="reveal-if-active">
                    <label for="input-text">Enter the text for Plagiarism Checking</label>
                    <textarea type="textarea" id="input-text" name="input-text" class="require-if-active" data-require-pair="#choice-text" onChange={e => this.handleTextarea(e)}></textarea>
                    <button type="button" class="btn btn-primary" style={{margin:"10px 0 10px 0", backgroundColor:"#4CAF50"}}onClick={e => this.handleTextSubmit(e)}>Submit</button>
                  </div>
                </div>
                <div>
                  <input type="radio" name="choice" id="choice-file" value="doc" onChange={e => this.handleRadioChange(e)} required />
                  <label for="choice-file" style={{paddingLeft:"10px"}}>Upload Text or Doc</label>
                  <div className="reveal-if-active">
                    <FileUpload 
                      name="file-upload"
                      multiple={false}
                      accept='.txt, .docx'
                      maxFileSize={10000000}
                      onUpload={e => this.handleFileUpload(e)}
                    /> 
                  </div>
                </div>
                <div>  
                  <input type="radio" name="choice" id="choice-ocr" value = "ocr" onChange={e => this.handleRadioChange(e)} required />
                  <label for="choice-ocr" style={{paddingLeft:"10px"}}>Upload Image (OCR)</label>
                  <div className="reveal-if-active">
                    <FileUpload 
                      name="file-upload"
                      multiple={false}
                      accept='.jpeg, .jpg, .png'
                      maxFileSize={10000000}
                      onUpload={e => this.handleFileUpload(e)}
                    /> 
                  </div>
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
