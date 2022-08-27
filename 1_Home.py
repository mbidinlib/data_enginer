
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
    """)
st.markdown("### Data Import")
st.markdown("""
    With the data import page, you would be able to import upto five (5) datasets for your work.
    Each dataset is in a seperate tab and you can navigate across tabs""")
st.markdown("### Check Duplicates")
st.markdown("""
    You can check if your data has dul=plicates using some key variables 
    and also remove duplicates if there are any
    """)
st.markdown("### Check Outliers")
st.markdown("""
    You can check if some variables have outliers given a certain multiplier effect
    """)
st.markdown("### Merge Data")
st.markdown("""
    This would help you to merge selected datasets that you imported into one. 
    You may also append datasets if needed
    """)

st.markdown("#### About Author")
st.markdown("""
    Visit the author's [GitHub page](github.com/mbidinlib) to see more works from the author
    """)
