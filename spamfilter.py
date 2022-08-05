# Import libraries
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


# Preparing text data
def handle_message(message): 
  # Step 1: Remove puntuation 
  message1 = [char for char in message if char not in string.punctuation]
  message1 = ''.join(message1)
  # Step 2: Remove stop word
  message2 = [word for word in message1.split() if word.lower() not in stopwords.words('english')]
  message2 = ' '.join(message2)
  # Step 3: Lemmatization
  lemmatizer = WordNetLemmatizer()
  word_list = nltk.word_tokenize(message2)
  result = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
  return result


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/spamfilter")
# Spam email handling funtions
async def spamfilter(message: str = Form()):
    filename = 'saved_model.pkl'
    # Loading trained models and count vectorizer
    with open(filename, 'rb') as f:
        model_import, cv_import = pickle.load(f)
    # Apply preprocessing to input message
    message = handle_message(message)
    array = [message]
    input = cv_import.transform(array)
    # Model predict if the message is spam or ham (non-spam)
    myprediction = model_import.predict(input)
    answer = myprediction[0]
    # Return a response with the prediction as content of the response
    return Response(status_code = 200, content= answer)