from fileinput import filename
from fastapi import FastAPI, Response, Form
import pickle
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from sklearn import svm
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
app = FastAPI()


def handle_message(message): #missing Lemmatization process
  # Step 1: lemmatization
  lemmatizer = WordNetLemmatizer()
  word_list = nltk.word_tokenize(message)
  message1 = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
  # Step 2: remove puntuation 
  message2 = [char for char in message1 if char not in string.punctuation]
  message2 = ''.join(message2)
  # Step 3: remove stop word
  message3 = [word for word in message2.split() if word.lower() not in stopwords.words('english')]
  result = ' '.join(message3)
  return result


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/spamfilter")
async def spamfilter(message: str = Form()):
    filename = 'saved_model.pkl'
    with open(filename, 'rb') as f:
        model_import, cv_import = pickle.load(f)
    message = handle_message(message)
    array = [message]
    input = cv_import.transform(array)
    myprediction = model_import.predict(input)
    print(myprediction)
    answer = myprediction[0]
    return Response(status_code = 200, content= answer)