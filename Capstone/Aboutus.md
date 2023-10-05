import streamlit as st #pip streamlit install
import pandas as pd
from PIL import Image

#Title
st.title("Nice to Meet You!")

image = Image.open('./IMG/A&T-Image.jpg')
st.image(image, use_column_width=True,)

st.header("We are class of 2023, we strive to assist our future Aggies in dealing with stresses of video games")
image = Image.open('./IMG/Graduation-pic.jpg')
st.image(image, use_column_width=True,)

st.header("Samiyia Floyd")
st.text("Major:Information Technology")
st.text("Classification:Senior")
st.text("Graduation:Fall 2023")

image = Image.open('./IMG/Samayia-Floyd.jpg')
st.image(image, use_column_width=True)


st.header("Antwune Gray")
st.text("Major:Information Technology")
st.text("Classification:Senior")
st.text("Graduation:Fall 2023")

image = Image.open('./IMG/Antwune-Gray.jpg')
st.image(image, use_column_width=True)




st.header("Jalen Thomas")
st.text("Major:Information Technology")
st.text("Classification:Senior")
st.text("Graduation:Spring 2024")

image = Image.open('./IMG/Jalen-Thomas.jpg')
st.image(image, use_column_width=True)


st.header("Mental Health Exploratory Data Analysis(EDA)")

st.subheader("Database system that shows how mental health has progressed to become better or worst from playing video games")
st.text("")
