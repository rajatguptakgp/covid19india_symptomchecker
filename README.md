# COVID-19 India Symptom Checker
Command Line Interface (CLi) chatbot prototype for assistance against COVID-19 pandemic

***
## Overview
This project is an experimental simulation of chatbot that works as COVID-19 screening tool which can help user understand what to do next about COVID-19.

## Features
- The chatbot prototype runs in the language of the user's region, location identified based on his/her IP Address.
- Available in multiple languages prominent in India.
- Once concluded that the user should visit a COVID-19 testing center, lists the details (Name, Address, Contact Number) about the nearest testing centre to him/her. Also, lists the details about other testing centres across each state in India. 

## Disclaimer 
```This tool is not intended to be used as a substitute for professional medical advice, diagnosis or treatment. Any reference to the Testing Centers has been taken through Google.```

## Reference
* [COVID-19 Symptom Checker](https://github.com/dylan-kuo/covid19-checker)

## Future Works
Migrate the functionality and deploy it to ChatBot using Flask.

## Installation
### Clone
Clone this repo to your local machine using `git clone https://github.com/rajatguptakgp/symptomchecker_covid19hackathon.git`

## Requirements
Since the program makes use of GeoPy and Googletrans, it is necessary to install them.<br /> 
Run the command `pip install -r requirements.txt` after making the covid19-checker folder working directory.<br /> 

IMPORTANT:  The program involves usage of fonts which are not available in command line, and hence it requires an IPython interface.

## Usage
### On Google Colab:
  1. Run `covid19-checker.ipynb` in Google Colab

### On your local machine:
  1. Open an IPython Kernel (in Jupyter Notebook or otherwise)
  2. Make the working directory to covid19-checker folder `cd <your path>/symptomchecker_covid19hackathon`<br />
  3. Fulfil all requirements by running `pip install -r requirements.txt`
  3. Run the python file using the command `run covid19-checker.py`

## Demo
Video Link: https://www.youtube.com/watch?v=6plPg48lCAM
