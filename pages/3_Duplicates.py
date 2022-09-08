
'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''

from io import StringIO
import pandas as pd
import streamlit as st
from io import BytesIO

# Options for excel imports
import pip
pip.main(["install", "openpyxl"])


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


          if sel_df != "":
               master_data = st.session_state[selected_df]

               # Check duplicates
               ##################
               with st.expander("Check Duplicates",expanded=False):
                         dup_data_vars = master_data.columns
                         dup_key = st.multiselect("Select the key variable. This can also be a combination of variables",dup_data_vars)
                         if dup_key:

                              # Query duplicates:
                              dup_data = master_data[master_data.duplicated(dup_key, keep = False)]
                              
                              # Add buttons
                              reportdups = st.button('Duplicates Report', key= 'reportdups')
                              viewdups = st.button(' View Duplicates', key= 'vewdups')
                              exportdups =  st.download_button(
                                             label="Export Duplicates",
                                             data=dup_data,
                                             file_name="Duplicates.xlsx",
                                             mime="application/vnd.ms-excel")


               with st.expander("Resolve Duplicates",expanded=False):
                         dup_data_vars = master_data.columns
                         #dupvars = st.multiselect("Select the key variable. This can also be a combination of variables",dup_data_vars, key='dupvars')




     #Column 2
     ##########################
     with col2:

          if sel_df != "":
               if dup_key and reportdups:
                    st.markdown(f"""Duplicates based on : <b><font style="color:#D9B604">{dup_key}</font></b>""",  
                    unsafe_allow_html=True)
               elif dup_key and (viewdups or exportdups):
                    st.markdown(f"""Duplicates based on : <b><font style="color:#D9B604">{dup_key}</font></b>""",  
                    unsafe_allow_html=True)
                    st.dataframe(dup_data)   # display duplicates data
               else:
                    st.markdown("Selected Dataset")
                    st.dataframe(master_data)            

# When No data has been inported
else:
     st.markdown("Go to the import page to import your dataset(s)")

