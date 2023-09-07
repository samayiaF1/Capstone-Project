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
st.header('From start to finish through the project we have come to find out two things. That videogames have positive and negative effects on an adolescents'' psychological state. Games like Fortnite, Call of Duty, and even NBA 2K can leave children with positive traits to transfer to the real world. Games such as Fortnite and Call of Duty which are first and third-person shooters help kids become better at decision making, spatial reasoning, and even attention spans even though to contrary belief of games reducing the attention span of children.')
st.info('Upload input data in the sidebar to start!')

# checkbox
st.checkbox("Disable text input widget", key="disabled")
st.session_state.disabled

#radio button
st.radio(
        "Set text input label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
)
st.session_state.visibility

#Scatter plot 
x1 = [1,2,3,4,5]
x2 = [10,22,13,34,25]
y= [100,200,50,60,80]
fig = plt.figure()
plt.scatter(x1, x2,
        c=y, alpha=0.8,
        cmap='viridis')

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()

#plt.show()
st.pyplot(fig)

#sidebar
dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('Iris', 'Breast Cancer', 'Wine')
)
st.write(f"## {dataset_name} Dataset")


