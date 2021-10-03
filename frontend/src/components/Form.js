import '../styles/App.css';
import '../styles/Form.scss'
import { FileUpload } from "primereact/fileupload"
import { Toast } from 'primereact/toast';
import { ProgressSpinner } from 'primereact/progressspinner';
import 'primereact/resources/themes/saga-green/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';
import React from 'react';
import LeftArrow from '../assets/arrow-left.png';

class Form extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      phase: "form",
      radio: "text",
      result: ""
    };
    this.handleRadioChange = this.handleRadioChange.bind(this);
    this.handleTextarea = this.handleTextarea.bind(this);
    this.handleTextSubmit = this.handleTextSubmit.bind(this);
  }

  handleRadioChange(event) {
    this.setState({radio: event.target.value});
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
        fetch("http://127.0.0.1:8000/api/form", {
          method: "POST",
          body: form_data
        })
          .then(data => data.json())
          .then(data => this.setState({result: data, phase: "result"}))
      }
    });
  }

  render() {
    if(this.state.phase === "form") {
      return (
        <div className="App">
          <header className="App-header">
            <Toast ref={(el) => this.toast = el} />
            <button type="button" className="btn back-button" onClick={(e) => this.props.history.push("/")}> <img src={LeftArrow} alt="Back" /> </button>
            <div className="Form-card">
              <div className="Form-name">PLAGIO</div>
              <form onSubmit={this.handleSubmit}>
                <div className="Form-heading">Choose your input</div>
                <div className="Form-choice">
                  <div>
                    <input type="radio" name="choice" id="choice-text" value="text" onChange={e => this.handleRadioChange(e)} required />
                    <label htmlFor="choice-text" style={{paddingLeft:"10px"}}>Text</label>
                    <div className="reveal-if-active">
                      <label htmlFor="input-text">Enter the text for Plagiarism Checking</label>
                      <textarea type="textarea" id="input-text" name="input-text" className="require-if-active" data-require-pair="#choice-text" onChange={e => this.handleTextarea(e)}></textarea>
                      <button type="button" className="btn btn-primary submit_text" style={{margin:"10px 0 10px 0", backgroundColor:"#4CAF50"}}onClick={e => this.handleTextSubmit(e)}>Submit</button>
                    </div>
                  </div>
                  <div>
                    <input type="radio" name="choice" id="choice-file" value="doc" onChange={e => this.handleRadioChange(e)} required />
                    <label htmlFor="choice-file" style={{paddingLeft:"10px"}}>Upload Text or Docx File</label>
                    <div className="reveal-if-active">
                      <FileUpload 
                        name="file-upload"
                        accept='.txt'
                        maxFileSize={10000000}
                        url={"http://127.0.0.1:8000/api/form"}
                        onSelect={(e) => {
                          this.setState({selectedFile: e.files[0]});
                        }}
                        onBeforeSend={(e)=> {
                          e.formData.append("mode", this.state.radio);
                          e.formData.append("file", this.state.selectedFile, this.state.selectedFile.name)
                          this.setState({phase: "loading"})
                        }}
                        onUpload={(e) => {
                          if(e.xhr.status === 200) {
                            let data = JSON.parse(e.xhr.response);
                            this.setState({result: data, phase: "result"})
                          } else {
                            this.toast.show({severity: "error", summary: "Unknown Error", detail:"An unknons exception has occured. Try Again.", life: 3000})
                          }
                        }}
                      /> 
                    </div>
                  </div>
                  <div>  
                    <input type="radio" name="choice" id="choice-ocr" value = "ocr" onChange={e => this.handleRadioChange(e)} required />
                    <label htmlFor="choice-ocr" style={{paddingLeft:"10px"}}>Upload Image (OCR)</label>
                    <div className="reveal-if-active">
                      <FileUpload 
                        name="file-upload"
                        accept='.jpeg, .jpg, .png'
                        maxFileSize={10000000}
                        url={"http://127.0.0.1:8000/api/form"}
                        onSelect={(e) => {
                            this.setState({selectedFile: e.files[0]});
                        }}
                        onBeforeSend={(e)=> {
                            e.formData.append("mode", this.state.radio);
                            e.formData.append("file", this.state.selectedFile, this.state.selectedFile.name)
                            this.setState({phase: "loading"})
                        }}
                        onUpload={(e) => {
                            if(e.xhr.status === 200) {
                              let data = JSON.parse(e.xhr.response);
                              this.setState({result: data, phase: "result"})
                            } else {
                              this.toast.show({severity: "error", summary: "Unknown Error", detail:"An unknons exception has occured. Try Again.", life: 3000})
                            }
                        }}
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
            <button type="button" className="btn btn-primary back-button" onClick={(e) => this.props.history.push("/")}> <img src={LeftArrow} alt="" /></button>
            <div className="Form-card">
              <div className="Form-name">PLAGIO</div>
              <ProgressSpinner style={{width: '70px', height: '70px', margin:'20px'}} strokeWidth="8" fill="#EEEEEE" animationDuration=".5s"/>
            </div>
          </header>
        </div>
      );
    } else if (this.state.phase === "result") {
      const result = this.state.result;
      let res = result.map(el => 
        <div className="PlagCard">
            <div className="PlagUrl"><a href={el["match"]}>{el["match"]}</a></div>
            <div className="PlagContent">{el["sentence"]}</div>
        </div>
      )
      return (
        <div className="App">
          <header className="App-header">
            <Toast ref={(el) => this.toast = el} />
            <button type="button" className="btn btn-primary back-button" onClick={(e) => this.props.history.push("/")}> <img src={LeftArrow} alt="" /></button>
            <div className="Form-card">
              <div className="Form-name">PLAGIO</div>
              <ol>
                {res}
              </ol>
            </div>
          </header>
        </div>
      );
    }
  }
}

export default Form;
