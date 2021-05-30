import '../styles/App.css';
import '../styles/Form.scss'
import { FileUpload } from "primereact/fileupload"
import { Toast } from 'primereact/toast';
import { ProgressSpinner } from 'primereact/progressspinner';
import 'primereact/resources/themes/saga-green/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';
import React from 'react';

class Form extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      phase: "form",
      radio: "text"
    };
    this.handleRadioChange = this.handleRadioChange.bind(this);
    this.handleFileUpload = this.handleFileUpload.bind(this);
    this.handleTextarea = this.handleTextarea.bind(this);
    this.handleTextSubmit = this.handleTextSubmit.bind(this);
  }

  handleRadioChange(event) {
    this.setState({radio: event.target.value});
  }

  handleFileUpload(event) {
    console.log("file uploaded")
    this.setState({ selectedFile: event.target.files[0], phase: "loading"}, () => {
      if(this.state.radio !== "ocr" || this.state.radio !== "doc") {
        this.toast.show({severity:'error', summary: 'Wrong option Selected', detail:'Select another option if you want to submit files', life: 3000});
      } else {
        event.preventDefault();
        let form_data = new FormData();
        form_data.append("file", this.state.selectedFile, this.state.selectedFile.name);
        form_data.append("mode", this.state.radio);
      }
    });
  }

  handleTextarea(event) {
    this.setState({ text: event.target.value})
  }

  handleTextSubmit(event) {
    this.setState({ phase: "loading" }, () => {
      if(this.state.radio !== "text") {
        this.toast.show({severity:'error', summary: 'Wrong option Selected', detail:'Select Text if you want to submit raw text', life: 3000});
      } else {
        event.preventDefault();
        let form_data = new FormData();
        form_data.append("text", this.state.text);
        form_data.append("mode", this.state.radio);
      }
    });
  }

  render() {
    if(this.state.phase === "form") {
      return (
        <div className="App">
          <header className="App-header">
            <Toast ref={(el) => this.toast = el} />
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
                    <label for="choice-file" style={{paddingLeft:"10px"}}>Upload Text or Docx File</label>
                    <div className="reveal-if-active">
                      <FileUpload 
                        name="file-upload"
                        accept='.txt'
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
    } else if (this.state.phase === "loading") {
      return (
        <div className="App">
          <header className="App-header">
            <Toast ref={(el) => this.toast = el} />
            <button type="button" class="btn btn-primary back-button" onClick={(e) => this.props.history.push("/")}>Back to Home Page</button>
            <div className="Form-card">
              <div className="Form-name">PLAGAWARE</div>
              <ProgressSpinner style={{width: '70px', height: '70px', margin:'20px'}} strokeWidth="8" fill="#EEEEEE" animationDuration=".5s"/>
            </div>
          </header>
        </div>
      );
    }
  }
}

export default Form;
