import streamlit as st
import pandas as pd
import numpy as np
import pickle
import re
import string

# Import the model
pickled_model = pickle.load(open('model.pkl', 'rb'))
pickled_model.predict(X_test)

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

    # functon to make prediction
    @st.cache
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
        new_xv_test = vectorization.transform(new_x_test)
        pred_LR = LR.predict(new_xv_test)
        pred_DT = DT.predict(new_xv_test)
        pred_GBC = GBC.predict(new_xv_test)
        pred_RFC = RFC.predict(new_xv_test)

        return print("\n\nLR Prediction: {} \nDT Prediction: {} \nGBC Prediction: {} \nRFC Prediction: {}".format(output_label(pred_LR[0]), 
                                                                                                              output_label(pred_DT[0]), 
                                                                                                              output_label(pred_GBC[0]), 
                                                                                                              output_label(pred_RFC[0])))
         

    # Declare a form to receive a movie's review
    form = st.form(key="my_form")
    review = form.text_input(label="Enter the text of your news")
    submit = form.form_submit_button(label="Make Prediction") 
     

