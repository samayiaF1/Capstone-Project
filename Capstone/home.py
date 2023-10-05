import streamlit as st #pip streamlit install
import pandas as pd
from PIL import Image

#Title
st.title('The Effects of video games on Adolescents' )

# Subheader
st.header('The study of whether video games can harm or help adolescents', 'Life of Brian')
# Show image
image = Image.open('./IMG/Brothers-Playing.png')
st.image(image, use_column_width=True)

# Subwriting
st.write('We have discovered through extensive research that video games have both positive and negative effects on adolescents psyche')

#Subheader
st.header('The beginning of research into video games and the effects on the brain')

st.write("At the University of Rochester, Daphne Bavelier and C. Shawn Green led the charge on video game research in the late 1990s. They started to investigate the outlandish hypothesis that video games might have an effect on neuroplasticity—a biological process in which the brain adapts and evolves in response to new experiences—and might even help with it.")
st.header("What negative affects do video games have on adolescents?")
st.write("As we already know that violent video games can encourage violent and aggressive behavior, but we wanted to know as to why and how do violent video games increase aggression ")

st.header("What did we learn?")

st.write('From start to finish through the project we have come to find out two things. That video games have positive and negative effects on an adolescents'' psychological state. Games like Fortnite, Call of Duty, and even NBA 2K can leave children with positive traits to transfer to the real world. Games such as Fortnite and Call of Duty which are first and third-person shooters help kids become better at decision making, spatial reasoning, and even attention spans even though to contrary belief of games reducing the attention span of children.')




st.header("Mental Health Exploratory Data Analysis(EDA)")

st.subheader("Database system that shows how mental health has progressed to become better or worst from playing video games")
st.text("")
