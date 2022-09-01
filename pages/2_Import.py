
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
        dfa1 = st.file_uploader("Select Data file", type=["csv", 'xlsx'])
    #Column two 
    with col2:
        if dfa1 is not None:
            try:
                st.session_state["dfa1"] = dfa1.getvalue().decode("utf-8")
            except:
                st.session_state["dfa1"] = dfa1.getvalue()
        if "dfa1" in st.session_state:
            st.header("Data overview")  # Give it a header
            df1= st.session_state["dfa1"]
            try:     # CSV            
                st.dataframe(pd.read_csv(StringIO(df1)))
            except: #xls , not yet finalized
                #st.dataframe(pd.read_excel(StringIO(df1)))
                st.write("This file is not a csv file. Support for Other file extentions would be added later")

