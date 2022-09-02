
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

with datatab1:
    col1, col2 = st.columns(2) #Split into two columns
    #Column one
    with col1:
        st.subheader("Select file")
        dataset1 = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data1")
        st.markdown("")
        st.markdown("")
        if "dataset1" in st.session_state:  # Add option to give name
            daset1_name = st.text_input("Short name of your dataset (optional)")

    #Column two 
    with col2:
        if dataset1 is not None:
            try:
                st.session_state["dataset1"] = dataset1.getvalue().decode("utf-8")
            except:
                st.session_state["dataset1"] = dataset1.getvalue()
        if "dataset1" in st.session_state:
            st.header("Data overview")  # Give it a header
            df1= st.session_state["dataset1"]
            try:     # CSV            
                st.dataframe(pd.read_csv(StringIO(df1)))
            except: #xls , not yet finalized
                #st.dataframe(pd.read_excel(StringIO(df1)))
                st.markdown("""**This file is not in csv format. Please select a csv file. 
                Support for Other file extensions would be added later**""")

with datatab2:
    col1, col2 = st.columns(2) #Split into two columns
    #Column one
    with col1:
        st.subheader("Select file")
        dataset2 = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data2")
        st.markdown("")
        st.markdown("")
        if "dataset1" in st.session_state:  # Add option to give name
            daset2_name = st.text_input("Short name of your dataset (optional)")
    #Column two 
    with col2:
        if dataset2 is not None:
            try:
                st.session_state["dataset2"] = dataset2.getvalue().decode("utf-8")
            except:
                st.session_state["dataset2"] = dataset2.getvalue()
        if "dataset2" in st.session_state:
            st.header("Data overview")  # Give it a header
            df2= st.session_state["dataset2"]
            try:     # CSV            
                st.dataframe(pd.read_csv(StringIO(df2)))
            except: #xls , not yet finalized
                #st.dataframe(pd.read_excel(StringIO(df1)))
                st.markdown("""**This file is not in csv format. Please select a csv file. 
                Support for Other file extensions would be added later**""")

