
import streamlit as st
import pickle 
import numpy as np
import sklearn

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Prediction")

    st.write("""### We need some information to predict the salary""")

