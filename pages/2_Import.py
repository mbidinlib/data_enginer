
'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''
from io import StringIO
import pandas as pd
import streamlit as st

st.markdown("# Import Data ")
#st.sidebar.markdown("# Import Data-")

datatab1, datatab2, datatab3, datatab4, datatab5 = st.tabs(["Dataset 1","Dataset 2", "Dataset 3", "Dataset 4","Dataset 5"])

##################
# Dataset 1 tab
##################

with datatab1:
    col1, col2 = st.columns(2) #Split into two columns
    #Column one
    with col1:
        st.subheader("Select file")
        dataset1 = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data1")
        st.markdown("")
        st.markdown("")
        
        # Preserve session state for selected file
        if dataset1 is not None:
            try:
                st.session_state["dataset1"] = dataset1.getvalue().decode("utf-8")
            except: #Excel
                st.session_state["dataset1"] = dataset1.getvalue()

        # Optional short name of dataset        
        if "dataset1" in st.session_state:  # Add option to give name
            dataset1_name = st.text_input("Short name of your dataset (optional). Default is **dataset1**", key="name1")
            if dataset1_name:
                st.session_state["dataset1_name"] = dataset1_name
            if 'dataset1_name' in st.session_state:
                #st.write(st.session_state["dataset1_name"])
                st.markdown(st.session_state["dataset1_name"])            
      
    #Column two 
    with col2:
        if "dataset1" in st.session_state:
            st.header("Data overview")  # Give it a header
            df1= st.session_state["dataset1"]
            try:     # CSV            
                st.dataframe(pd.read_csv(StringIO(df1)))
            except: #xls , not yet finalized
                #st.dataframe(pd.read_excel(StringIO(df1)))
                st.markdown("""**This file is not in csv format. Please select a csv file. 
                Support for Other file extensions would be added later**""")

##################
# Dataset 2 tab
##################
with datatab2:
    col1, col2 = st.columns(2) #Split into two columns
    #Column one
    with col1:
        st.subheader("Select file")
        dataset2 = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data2")
        st.markdown("")
        st.markdown("")
        
        # Preserve session state for selected file
        if dataset2 is not None:
            try:
                st.session_state["dataset2"] = dataset2.getvalue().decode("utf-8")
            except: #Excel
                st.session_state["dataset2"] = dataset2.getvalue()

        # Optional short name of dataset        
        if "dataset2" in st.session_state:  # Add option to give name
            dataset2_name = st.text_input("Short name of your dataset (optional). The default is **dataset2**", key="name2")
            if dataset2_name:
                st.session_state["dataset2_name"] = dataset2_name
            if 'dataset2_name' in st.session_state:
                #st.write(st.session_state["dataset2_name"])
                st.markdown(st.session_state["dataset2_name"])            
      
    #Column two 
    with col2:
        if "dataset2" in st.session_state:
            st.header("Data overview")  # Give it a header
            df2= st.session_state["dataset2"]
            try:     # CSV            
                st.dataframe(pd.read_csv(StringIO(df2)))
            except: #xls , not yet finalized
                #st.dataframe(pd.read_excel(StringIO(df1)))
                st.markdown("""**This file is not in csv format. Please select a csv file. 
                Support for Other file extensions would be added later**""")
