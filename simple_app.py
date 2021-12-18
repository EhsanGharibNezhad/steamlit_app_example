import pickle
import streamlit as st
import sklearn

st.title("Which author do you write like?")

with open("models/mnb_pipe.pkl", mode='rb') as pickle_in:
    pipe = pickle.load(pickle_in)

user_text = st.text_input("Please write some text:")

prediction = pipe.predict([user_text])[0] # We're using [0] to index the array and get only the string

st.write(f"You write like {prediction}.")
