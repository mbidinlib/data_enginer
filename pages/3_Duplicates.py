
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

col1, col2 = st.columns((1,2))

if ("dataset1" in st.session_state or "dataset2" in st.session_state or "dataset3" in st.session_state or 
     "dataset4" in st.session_state or "dataset4" in st.session_state):
    
     #Get short name of datasets
     #############################
     #Dataset 1
     if "dataset1" not in st.session_state:
          ds1=""
     else:
          try:
               ds1 = st.session_state["dataset1_name"]
          except:
               ds1 = "dataset1"
     #Dataset 2
     if "dataset2" not in st.session_state:
          ds2=""
     else:
          try:
               ds2 = st.session_state["dataset2_name"]
          except:
               ds2 = "dataset2"
     #Dataset 3
     if "dataset3" not in st.session_state:
          ds3=""
     else:
          try:
               ds3 = st.session_state["dataset3_name"]
          except:
               ds3 = "dataset3"
     #Dataset 4
     if "dataset4" not in st.session_state:
          ds4=""
     else:
          try:
               ds4 = st.session_state["dataset4_name"]
          except:
               ds4 = "dataset4"
     #Dataset 5
     if "dataset5" not in st.session_state:
          ds5=""
     else:
          try:
               ds5 = st.session_state["dataset5_name"]
          except:
               ds5 = "dataset5"

     with col1:
          #Selecting dataset to use
          ###########################
          sel_df = st.selectbox(
               'Select the dataset you want to check',
               [ds1, ds2, ds3, ds4, ds5])
          if sel_df == ds1 :
               selected_df = "dataset1" 
          elif sel_df == ds2:
               selected_df = "dataset2"
          elif sel_df == ds3:
               selected_df = "dataset3"
          elif sel_df == ds4:
               selected_df = "dataset4"
          elif sel_df == ds5:
               selected_df = "dataset5"

          with st.expander("Check Duplicates",expanded=False):
               try:
                    dup_data= pd.read_csv(st.session_state[selected_df])             
                    #st.dataframe(dup_data)
               except:
                    dup_data_vars =   ""  
                    #dup_data= pd.read_excel(st.session_state[selected_df])
               #dup_data_vars = dup_data.columns
               #options = st.multiselect(dup_data_vars)



     #Column 2
     ##########################
     with col2: 
               dup_data= pd.read_csv(StringIO(st.session_state["dataset1"]))             
     
if "dataset1" not in st.session_state or "dataset2" not in st.session_state:
     st.markdown("Go to the import page to import your dataset(s)")

