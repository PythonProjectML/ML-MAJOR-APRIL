
# It is a magic command to create a .py file
import streamlit as st
import joblib
model = joblib.load('spam-ham')
st.title('SPam Ham Classifier')
ip = st.text_input("Enter the message")
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0]) 
