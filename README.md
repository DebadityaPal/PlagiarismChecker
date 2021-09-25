
# Plagio: An OCR enabled Plagiarism Checker
With the spread of the COVID-19 pandemic, the world is observing a shift in the paradigm of the system of education as more institutions adopt online and cloud-based systems of teaching and evaluation. However, this change comes with its pitfalls, one of the most prominent being the inability to check for plagiarism effectively in answer sheets, especially if it is handwritten. Our proposed software involves an Optical Character Recognition (OCR) system that can extract textual data from scanned images of pages with handwritten information on them. Then the extracted data is checked for plagiarism against a database of approximately 130 trillion web pages, and a final report is generated.

## Flow of Data
There are 3 main modules to the project:
 1. OCR Module
 2. Plagiarism Checker Module
 3. Website
 
And the internal data flow is depicted by the following block diagram.
<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1TO8rb0G6O5YKRLGn82PyfzScsiVyM19C" width="600"/>
</p>

## How to set up

 1. Clone the repository using `git clone https://github.com/DebadityaPal/PlagiarismChecker`
 2. Move into the directory using `cd PlagiarismChecker`
 3. Install all dependencies for the backend using `pip install -r requirements.txt`
 4. Move into the frontend folder using `cd frontend`
 5. Install all dependencies for the frontend using `npm install`

## How to run the software
### Backend
1. Move into the backend folder from the root folder using `cd backend`
2. Run the server using `python manage.py runserver 8000`
It is important to start the server at port 8000, otherwise frontend requests might not be served.

### Frontend
1. Move into the backend folder from the root folder using `cd frontend`
2. Run the server using `npm run start`
