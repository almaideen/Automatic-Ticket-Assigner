import re
import pickle
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import nltk
from nltk.tokenize import word_tokenize
nltk.download('wordnet', download_dir='/home/appuser/nltk_data/')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

#Loading Vectorizer
with open('vectorizer.pkl','rb') as f:
    vectorizer = pickle.load(f)

#Loading Model
with open('model.pkl','rb') as f:
    model = pickle.load(f)

#Set up streamlit app

st.set_page_config(page_title='Ticket Assigner')
st.title('Automatic Ticket Assigner')
st.sidebar.header('Teams handling Tickets')
st.sidebar.write('Debt collection')
st.sidebar.write('Consumer Reports')
st.sidebar.write('Credit card')
st.sidebar.write('Accounts')
st.sidebar.write('Loan')
st.sidebar.write('Mortgage')
st.sidebar.write('Money Trasfer')

input_text = st.text_area('Please Enter your complaint here.')
data = [input_text]
if st.button('Submit'):
    data1 = re.sub('[^a-z A-Z 0-9-]+','',str(data))
    data2 = " ".join(data1.split())
    word_tokens = word_tokenize(data2)
    data3 = []
    for i in word_tokens:
        data3.append(lemmatizer.lemmatize(i,pos="v"))
    data4 = " ".join(data3)
    data5 = [data4]
    vectors = vectorizer.transform(data5).toarray()
    prediction = model.predict(vectors)

    if prediction[0] == 0:
        st.write('Your complaint has been registred successfully and the ticket is assigned to Debt Collection Team')
    elif prediction[0] == 1:
        st.write('Your complaint has been registered successfully and the ticket is assigned to Consumer Reports Team')
    elif prediction[0] == 2:
        st.write('Your complaint has been registered successfully and the ticket is assigned to Credit Card Team')
    elif prediction[0] == 3:
        st.write('Your complaint has been registered successfully and the ticket is assigned to Accounts Team')
    elif prediction[0] == 4:
        st.write('Your Complaint has been registered successfully and the ticket is assigned to Loan Team')
    elif prediction[0] == 5:
        st.write('Your Complaint has been registered successfully and the ticket is assigned to Mortgage Team')
    elif prediction[0]==6:
        st.write('Your Complaint has been registered successfully and the ticket is assigned to Money Transfer Team')

    
