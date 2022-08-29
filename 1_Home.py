
'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import time as tm


#Installed programs
#npm install streamlit-component-lib

#Add background image
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://github.com/mbidinlib/data_enginer/blob/main/picture.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

#st.sidebar.markdown("# Home page")
with st.sidebar.container():
    st.image('picture.jpg',
    caption='Mathew Bidinlib', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    #st.image(image, width= use_column_width=True)

st.markdown("# MGlory Data Engineering Toolkit ")
st.markdown("""
    Welcome to MGlory Data Engineering toolkit.
    This is a python based tool that would help you prepare your dataset for analysis.
    The tool contains the following components:
    - **Data Import**
    With the data import page, you would be able to import upto five (5) datasets for your work.
    Each dataset is in a seperate tab and you can navigate across tabs
    - **Check Duplicates**
    You can check if your data has dul=plicates using some key variables 
    and also remove duplicates if there are any
    - **Check Outliers**
    You can check if some variables have outliers given a certain multiplier effect
    - **Merge Data**
    This would help you to merge selected datasets that you imported into one. 
    You may also append datasets if needed
    """)
