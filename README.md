# FHIRDocumentGenerator
Generates Patient Health Records after accessing GOSH DRIVE’s FHIR server.

# Deployment
1) Create a virtual environment in the same folder as the requirements.txt file and
 activate the environment. Please see here for information on creating a 
 virtual environment: https://docs.python.org/3/tutorial/venv.html . 
 The virtual environment is desirable but not essential.
 
2) Run ‘pip install -r requirements.txt’ on terminal/cmd. This should install all packages required
   for this project

3) Run document_api.py to host the api on localhost

4) Leave this running

5) Run the Controller.py file.

# Solution
1) The Fhir_api/document_api.py is the RESTful api i've created to 
host data on local host after getting data from GOSH DRIVE’s FHIR server.

2) The Patient Forms software package gets data hosted by my api,
generating a document once a valid patient id in inputted.
 
Creates a popup window.

Input a valid patient id and click generate patient record. 
This creates a word document of the patient's health record with
only vital-signs shown. This folder would be created in the
filePath specified by the user of the DocumentGenerator class

Click all patient graph and a graph that plots the 
frequency of the people that are married or not or speak
english per age is plotted. Please see Frequency graph.pdf