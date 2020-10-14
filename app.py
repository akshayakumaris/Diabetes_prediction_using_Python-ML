# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:31:21 2020

@author: user
"""
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import streamlit as st
from PIL import Image
import pandas as pd
import pickle

pickle_in=open('RFC.pkl','rb')
loaddata=pickle.load(pickle_in)

def get_user_input():
    preg=st.sidebar.slider('pregnancies',0,17,3)
    glu=st.sidebar.slider('Glucose',0,199,117)
    bp=st.sidebar.slider('BloodPressure',0,122,72)
    skin=st.sidebar.slider('SkinThickness',0,99,23)
    insu=st.sidebar.slider('Insulin',0.0,846.0,30.0)
    bmi=st.sidebar.slider('BMI',0.0,67.1,32.0)
    dpf=st.sidebar.slider('DPF',0.078,2.42,0.375)
    age=st.sidebar.slider('age',21,81,29)
    
    user_data={
        'pregnancies':preg,
        'glucose':glu,
        'blood_pressure':bp,
        'skin_thickness':skin,
        'insulin':insu,
        'BMI':bmi,
        'DPF':dpf,
        'age':age
        }
    
    features=pd.DataFrame(user_data,index= [0] )
    return features

def main():
    st.title("""
    #DIABETES DETECTION WEB APP
    *Using Python and Machine Learning technique!!!*         
    """)
    
    image=Image.open('D.jpg')
    st.image(image,caption='using streamlit,python,ML',use_column_width=True)
    
    st.subheader('Data Information:')
    df=pd.read_csv('diabetes.csv')

    st.dataframe(df)
    
    st.write(df.describe())
    
    chart=st.bar_chart(df)
    
    user_input=get_user_input()
    st.write("\n")
    
    st.subheader('user Input:')
    st.write(user_input)
    st.write("\n")
    st.write("\n")
    st.write("\n")
    predictions=loaddata.predict(user_input)

    st.subheader('Classification:')
    
    if predictions==1:
        
        st.success('The Person with given input data *found diabetes*')
    
    elif predictions==0:
        st.success('The Person with given input data *found no diabetes*')



if __name__=='__main__':
    main()