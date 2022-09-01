
'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''

from io import StringIO
import pandas as pd
import streamlit as st

#Import pages
#from streamlit_multipage import MultiPage


st.markdown("# Check Duplicates ")
st.sidebar.markdown("# Check Duplicates-")

if ("dataset1" in st.session_state or "dataset2" in st.session_state or "dataset3" in st.session_state or 
     "dataset4" in st.session_state or "dataset4" in st.session_state):

     selected_df = st.selectbox(
          'Select the dataset you want to check',
          ("dataset1", "dataset2", "dataset3", "dataset4", "dataset5"))

     try:
          dup_data= pd.read_csv(StringIO(st.session_state[selected_df]))             
          st.dataframe(dup_data)
     except Exception as e: # Excel version
          print(e)
          #dup_data= pd.read_csv(StringIO(st.session_state["dataset1"]))             
     
if "dataset1" not in st.session_state or "dataset2" not in st.session_state:
     st.markdown("Go to the import page to import your dataset(s)")

