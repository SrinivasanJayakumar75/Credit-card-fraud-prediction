import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image



model = pickle.load(open('model.pkl', 'rb'))

st.title('Credit Card Fraud Prediction')

image = Image.open('creditcard.jpg')
st.image(image, 'CREDITCARD')


def user_report():
    Time = st.text_input('Time')
    V12 = st.text_input('V12')
    V14 = st.text_input('V14')
    V9 = st.text_input('V9')
    V15 = st.text_input('V15')
    V17 = st.text_input('V17')
    V11 = st.text_input('V11')
    V26 = st.text_input('V26')
    V16 = st.text_input('V16')
    V7 = st.text_input('V7')
    V18 = st.text_input('V18')
    V3 = st.text_input('V3')
    Amount = st.text_input('Amount')
    


    user_report_data = {
        'Time':Time,
        'V12':V12,
        'V14':V14,
        'V9':V9,
        'V15':V15,
        'V17':V17,
        'V11':V11,
        'V26':V26,
        'V16':V16,
        'V7':V7,
        'V18':V18,
        'V3':V3,
        'Amount':Amount
    }   
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data


user_data = user_report()


if st.button("predict"):
     model.predict(user_data)
     st.write(model.predict(user_data))             






   

