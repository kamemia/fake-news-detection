import streamlit as st
import pandas as pd
import numpy as np
import pickle


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

if app_mode=='Home':
    st.title('Fake News Prediction:')  
    st.image('Newspaper.jpg')
    st.markdown('Dataset :')
    data=pd.read_csv('data/fake.csv')
    st.write(data.head())
