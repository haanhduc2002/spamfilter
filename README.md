# Spam filtering practical project
## Introduction

This project is my practical assignment for IT Security Course at Swinburne University of Techonology Vietnam.

In this project, trained a Support Vector Machine (SVM) technique to filter spam email message and implement my model on an API written in FastAPI and run on a simple web server using Uvicorn.

## Libraries used

Data manipulation: [pandas](https://pandas.pydata.org/), [numpy](https://numpy.org/)

Data visualization: [matplotlib](https://matplotlib.org/)

Natural Language Processing: [nltk](https://www.nltk.org/)

## Installation

After cloning this repository, go to the root folder of this repository then enter into the terminal:

```
pip install --upgrade pip
pip install -r requirements.txt
```
## Usage

Go to the root folder of this repository then enter into the terminal:
```
uvicorn spamfilter:app --reload
```
Open your web browser then type into the address bar
```
http://127.0.0.1:8000/docs
```
This allow the user to have the overview of all API endpoints and test them imteractively by using the Swagger document embedded into FastAPI


