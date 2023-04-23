import streamlit as st
import pandas as pd
import numpy as np
import os
import time
from matplotlib import image





path1=os.getcwd()
path2=os.path.join(path1,'resources','pub.csv')
dir_of_interest1 = os.path.join(path1,"resources","image pub.jpg")


df = pd.read_csv(path2)
st.set_page_config(layout="wide")
st.title(':grey[🥂Pubs In United Kingdom Is To Have Some Drink And Chillout🥂]')
st.subheader(":green[About me : :wave: ]")
col1,col2,col3=st.columns(3, gap='small')
with col1:
    st.subheader("[LinkedIn](https://www.linkedin.com/in/afreen-banu/)")
with col2:
    st.subheader("[GitHub](https://github.com/AfreenBanu085)")
with col3:
    if st.button('Biodata'):
       
        st.markdown('''
        Name: Afreen Banu
        
        Education : B.Tech(Electronic and Communication Engineering)
        
        Aspiring Data Scientist''')
        


latitude = st.text_input('Enter the lattitude')
longitude = st.text_input('Enter the longitude')

arr = np.array(df[['latitude','longitude']])

if latitude and longitude:
    point = [float(latitude),float(longitude)]
    df['distance'] = np.sqrt(np.sum((arr-point)**2,axis=1))
    df = df.sort_values(by='distance')
    df[['latitude','longitude',"name","address",'postcode','local_authority']][:5]
    st.map(df[['latitude','longitude']][:5])
    #Unique Bars and Local Authorities
unique=['Number of Pubs','Number of Postal Code']

option=st.radio(label="Select below options to see total count",
                options=unique,label_visibility="visible", horizontal=True)

if option=='Number of Pubs':
    st.subheader(f"Total Pubs in UK: :green[{df['name'].nunique()}]")
elif option=='Number of Postal Code':
    st.subheader(f"Total Post Codes in UK: :green[{df['PostCode'].nunique()}]")


st.subheader(":blue[Pubs are at the heart of British communities and serve as places for friends to gather, people to relax and unwind stories to be told 🍹🥂🍹.]")
img = image.imread(dir_of_interest1)
st.image(img)
