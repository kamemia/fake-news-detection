import streamlit as st
import pandas as pd
import numpy as np
import pickle
import re
import string

# Creating a menu tab 

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction'])

# Creating a Homepage

if app_mode=='Home':
    st.title('Fake News Prediction:')  
    st.image('Newspaper.jpg')
    st.markdown('Dataset for fake news:')
    data=pd.read_csv('data/fake.csv')
    st.write(data.head())
    st.markdown('Dataset for true news:')
    data=pd.read_csv('data/True.csv')
    st.write(data.head())

# Creating a Prediction page

elif app_mode == 'Prediction':
    st.title('Predict the news')

    # Functon to make prediction
    @st.cache
    def word_drop(text):
        text = text.lower()
        text = re.sub('\[.*?\]', '',text)
        text = re.sub("\\W", " ",text)
        text = re.sub('https?://\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        return text

    def output_label(n):
        if n == 0:
            return 'Fake News'
        elif n == 1:
            return 'Not fake News'
    
    def manual_testing(news):
        testing_news = {'text':[news]}
        new_def_test = pd.DataFrame(testing_news)
        new_def_test['text'] = new_def_test['text'].apply(word_drop)
        new_x_test = new_def_test['text']
         

    news = st.text_input("Enter the news", "Type Here..")

    if(st.button('Submit')):
        result = news.title()
        st.success(result)