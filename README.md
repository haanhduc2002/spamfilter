# Spam filtering practical project
## Introduction

This project is my practical assignment for IT Security Course at Swinburne University of Techonology Vietnam.

In this project, trained a Support Vector Machine (SVM) technique to filter spam email message and implement my model on an API written in FastAPI and run on a simple web server using Uvicorn.

A notebook where I visualize the data set and trained the model is on [Google Colab](https://colab.research.google.com/drive/1CMVaStWbFMBAdRODyfH882taOfr9nUzl?authuser=3#scrollTo=WThM9OV-Usgw). You can run this notebook in case there are any problems with the notebook in this repository

## Modules used

Data manipulation: [pandas](https://pandas.pydata.org/), [numpy](https://numpy.org/)

Data visualization: [matplotlib](https://matplotlib.org/)

Natural Language Processing: [nltk](https://www.nltk.org/)

Machine Learning: [SKLearn](https://scikit-learn.org/stable/index.html)

Creating API: [FastAPI](https://fastapi.tiangolo.com/)

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


