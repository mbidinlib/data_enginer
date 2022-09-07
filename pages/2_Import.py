
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
    col1, col2 = st.columns((1,2)) #Split into two columns
    #Column one
    with col1:
        st.subheader("Select file")
        dataset1 = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data1")
        st.markdown("")
        st.markdown("")
        
        # Preserve session state for selected file
        if dataset1 is not None:
            st.session_state["dataset1"] = dataset1 #.getvalue().decode("utf-8")

        # Optional short name of dataset        
        if "dataset1" in st.session_state:  # Add option to give name
            dataset1_name = st.text_input("Short name of your dataset (optional). Default is *dataset1*", key="name1")
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
                st.dataframe(pd.read_csv(df1,dtype='unicode')) ### Remove
                #st.dataframe(pd.read_csv(StringIO(df1),dtype='unicode')) ### Remove
            except: #xls , not yet finalized
                st.dataframe(pd.read_excel(df1))
                #st.markdown("""**This file is type is currently not accepted. Upload a file with a .csv or xls extenssion. 
                #Support for Other file extensions would be added later**""")

##################
# Dataset 2 tab
##################
with datatab2:
    col1, col2 = st.columns((1,2)) #Split into two columns
    #Column one
    with col1:
        st.subheader("Select file")
        dataset2 = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data2")
        st.markdown("")
        st.markdown("")
        
        # Preserve session state for selected file
        if dataset2 is not None:
            st.session_state["dataset2"] = dataset2 #.getvalue().decode("utf-8")
        # Optional short name of dataset        
        if "dataset2" in st.session_state:  # Add option to give name
            dataset2_name = st.text_input("Short name of your dataset (optional). The default is *dataset2*", key="name2")
            if dataset2_name:
                st.session_state["dataset2_name"] = dataset2_name
            if 'dataset2_name' in st.session_state:
                #st.write(st.session_state["dataset2_name"])
                st.markdown(st.session_state["dataset2_name"])            
      
    #Column two 
    with col2:
        if "dataset2" in st.session_state:
            st.header("Data overview")  # Give it a header
            df2 = st.session_state["dataset2"]
            try:     # CSV            
                st.dataframe(pd.read_csv(df2,dtype='unicode'))
            except: #xls , not yet finalized
                st.dataframe(pd.read_excel(df1))
                st.markdown("""**This file is type is currently not accepted. Upload a file with a .csv or xls extenssion. 
                Support for Other file extensions would be added later**""")

##################
# Dataset 3 tab
##################
with datatab3:
    col1, col2 = st.columns((1,2)) #Split into two columns
    #Column one
    with col1:
        st.subheader("Select file")
        dataset3 = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data3")
        st.markdown("")
        st.markdown("")
        
        # Preserve session state for selected file
        if dataset3 is not None:
            st.session_state["dataset3"] = dataset3 #.getvalue().decode("utf-8")
        # Optional short name of dataset        
        if "dataset3" in st.session_state:  # Add option to give name
            dataset3_name = st.text_input("Short name of your dataset (optional). The default is *dataset3*", key="name3")
            if dataset3_name:
                st.session_state["dataset3_name"] = dataset3_name
            if 'dataset3_name' in st.session_state:
                #st.write(st.session_state["dataset2_name"])
                st.markdown(st.session_state["dataset3_name"])            
      
    #Column two 
    with col2:
        if "dataset3" in st.session_state:
            st.header("Data overview")  # Give it a header
            df3= st.session_state["dataset3"]
            try:     # CSV            
                st.dataframe(pd.read_csv(df3,dtype='unicode'))
            except: #xls , not yet finalized
                st.dataframe(pd.read_excel(df1))
                st.markdown("""**This file is type is currently not accepted. Upload a file with a .csv or xls extenssion. 
                Support for Other file extensions would be added later**""")

##################
# Dataset 4 tab
##################
with datatab4:
    col1, col2 = st.columns((1,2)) #Split into two columns
    #Column one
    with col1:
        st.subheader("Select file")
        dataset4 = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data4")
        st.markdown("")
        st.markdown("")
        
        # Preserve session state for selected file
        if dataset4 is not None:
            st.session_state["dataset4"] = dataset4

        # Optional short name of dataset        
        if "dataset4" in st.session_state:  # Add option to give name
            dataset4_name = st.text_input("Short name of your dataset (optional). The default is *dataset4*", key="name4")
            if dataset4_name:
                st.session_state["dataset4_name"] = dataset4_name
            if 'dataset4_name' in st.session_state:
                #st.write(st.session_state["dataset2_name"])
                st.markdown(st.session_state["dataset4_name"])            
      
    #Column two 
    with col2:
        if "dataset4" in st.session_state:
            st.header("Data overview")  # Give it a header
            df4= st.session_state["dataset4"]
            try:     # CSV            
                st.dataframe(pd.read_csv(df4,dtype='unicode'))
            except: #xls , not yet finalized
                st.dataframe(pd.read_excel(df1))
                st.markdown("""**This file is not in csv format. Please select a csv file. 
                Support for Other file extensions would be added later**""")

##################
# Dataset 5 tab
##################
with datatab5:
    col1, col2 = st.columns((1,2)) #Split into two columns
    #Column one
    with col1:
        st.subheader("Select file")
        dataset5 = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data5")
        st.markdown("")
        st.markdown("")
        
        # Preserve session state for selected file
        if dataset5 is not None:
            st.session_state["dataset5"] = dataset5 #.getvalue().decode("utf-8")

        # Optional short name of dataset        
        if "dataset5" in st.session_state:  # Add option to give name
            dataset5_name = st.text_input("Short name of your dataset (optional). The default is *dataset5*", key="name5")
            if dataset5_name:
                st.session_state["dataset5_name"] = dataset5_name
            if 'dataset5_name' in st.session_state:
                #st.write(st.session_state["dataset5_name"])
                st.markdown(st.session_state["dataset5_name"])            
      
    #Column two 
    with col2:
        if "dataset5" in st.session_state:
            st.header("Data overview")  # Give it a header
            df5= st.session_state["dataset5"]
            try:     # CSV            
                st.dataframe(pd.read_csv(df5, dtype='unicode'))
            except: #xls , not yet finalized
                st.dataframe(pd.read_excel(df1))
                st.markdown("""**This file is not in csv format. Please select a csv file. 
                Support for Other file extensions would be added later**""")
