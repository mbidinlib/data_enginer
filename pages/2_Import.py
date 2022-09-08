
'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''
from io import StringIO
import pandas as pd
import streamlit as st

# Options for excel imports
import pip
pip.main(["install", "openpyxl"])

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
        ds1 = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data1")
        st.markdown("")
        st.markdown("")
        
        # Preserve session state for selected file
        if ds1 is not None:
            st.session_state["ds1"] = ds1 #.getvalue().decode("utf-8")

        # Optional short name of dataset        
        if "ds1" in st.session_state:  # Add option to give name
            ds1_name = st.text_input("Short name of your dataset (optional). Default is *ds1*", key="name1")
            if ds1_name:
                st.session_state["ds1_name"] = ds1_name
            if 'ds1_name' in st.session_state:
                #st.write(st.session_state["ds1_name"])
                st.markdown(st.session_state["ds1_name"])   
      
    #Column two 
    with col2:
        if "ds1" in st.session_state:
            st.header("Data overview")  # Give it a header
            df1= st.session_state["ds1"]
            file_ext1 = df1.name.split('.')[-1]  # get file extension of selected file
            st.markdown(file_ext1) # remove

            if file_ext1 == 'csv':
               dataset1 = pd.read_csv(df1,dtype='unicode')
               st.dataframe(dataset1) 
                #st.dataframe(pd.read_csv(StringIO(df1),dtype='unicode')) ### Remove                           
            elif file_ext1 == 'xls'or file_ext1 == 'xlsx': #xls , not yet finalized
                dataset1 = pd.read_excel(df1, engine='openpyxl').astype(str)
                st.dataframe()
                #st.dataframe(pd.read_excel(df1))
            else:
                st.markdown("""**This file is type is currently not accepted. Upload a file with a .csv or xls extenssion. 
                #Support for Other file extensions would be added later**""")

##################
# Dataset 2 tab
##################
with datatab2:
    col1, col2 = st.columns((1,2)) #Split into two columns
    #Column one
    with col1:
        st.subheader("Select file")
        ds2 = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data2")
        st.markdown("")
        st.markdown("")
        
        # Preserve session state for selected file
        if ds2 is not None:
            st.session_state["ds2"] = ds2 #.getvalue().decode("utf-8")
        # Optional short name of dataset        
        if "ds2" in st.session_state:  # Add option to give name
            ds2_name = st.text_input("Short name of your dataset (optional). The default is *ds2*", key="name2")
            if ds2_name:
                st.session_state["ds2_name"] = ds2_name
            if 'ds2_name' in st.session_state:
                #st.write(st.session_state["ds2_name"])
                st.markdown(st.session_state["ds2_name"])            
      
    #Column two 
    with col2:
        if "ds2" in st.session_state:
            st.header("Data overview")  # Give it a header
            df2 = st.session_state["ds2"]
            try:     # CSV            
                st.dataframe(pd.read_csv(df2,dtype='unicode'))
            except: #xls , not yet finalized
                st.dataframe(pd.read_excel(df2, engine='openpyxl').astype(str))

##################
# Dataset 3 tab
##################
with datatab3:
    col1, col2 = st.columns((1,2)) #Split into two columns
    #Column one
    with col1:
        st.subheader("Select file")
        ds3 = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data3")
        st.markdown("")
        st.markdown("")
        
        # Preserve session state for selected file
        if ds3 is not None:
            st.session_state["ds3"] = ds3 #.getvalue().decode("utf-8")
        # Optional short name of dataset        
        if "ds3" in st.session_state:  # Add option to give name
            ds3_name = st.text_input("Short name of your dataset (optional). The default is *ds3*", key="name3")
            if ds3_name:
                st.session_state["ds3_name"] = ds3_name
            if 'ds3_name' in st.session_state:
                #st.write(st.session_state["ds2_name"])
                st.markdown(st.session_state["ds3_name"])            
      
    #Column two 
    with col2:
        if "ds3" in st.session_state:
            st.header("Data overview")  # Give it a header
            df3= st.session_state["ds3"]
            try:     # CSV            
                st.dataframe(pd.read_csv(df3,dtype='unicode'))
            except: #xls , not yet finalized
                st.dataframe(pd.read_excel(df3, engine='openpyxl').astype(str))

##################
# Dataset 4 tab
##################
with datatab4:
    col1, col2 = st.columns((1,2)) #Split into two columns
    #Column one
    with col1:
        st.subheader("Select file")
        ds4 = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data4")
        st.markdown("")
        st.markdown("")
        
        # Preserve session state for selected file
        if ds4 is not None:
            st.session_state["ds4"] = ds4

        # Optional short name of dataset        
        if "ds4" in st.session_state:  # Add option to give name
            ds4_name = st.text_input("Short name of your dataset (optional). The default is *ds4*", key="name4")
            if ds4_name:
                st.session_state["ds4_name"] = ds4_name
            if 'ds4_name' in st.session_state:
                #st.write(st.session_state["ds2_name"])
                st.markdown(st.session_state["ds4_name"])            
      
    #Column two 
    with col2:
        if "ds4" in st.session_state:
            st.header("Data overview")  # Give it a header
            df4= st.session_state["ds4"]
            try:     # CSV            
                st.dataframe(pd.read_csv(df4,dtype='unicode'))
            except: #xls , not yet finalized
                st.dataframe(pd.read_excel(df4, engine='openpyxl').astype(str))

##################
# Dataset 5 tab
##################
with datatab5:
    col1, col2 = st.columns((1,2)) #Split into two columns
    #Column one
    with col1:
        st.subheader("Select file")
        ds5 = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data5")
        st.markdown("")
        st.markdown("")
        
        # Preserve session state for selected file
        if ds5 is not None:
            st.session_state["ds5"] = ds5 #.getvalue().decode("utf-8")

        # Optional short name of dataset        
        if "ds5" in st.session_state:  # Add option to give name
            ds5_name = st.text_input("Short name of your dataset (optional). The default is *ds5*", key="name5")
            if ds5_name:
                st.session_state["ds5_name"] = ds5_name
            if 'ds5_name' in st.session_state:
                #st.write(st.session_state["ds5_name"])
                st.markdown(st.session_state["ds5_name"])            
      
    #Column two 
    with col2:
        if "ds5" in st.session_state:
            st.header("Data overview")  # Give it a header
            df5= st.session_state["ds5"]
            try:     # CSV            
                st.dataframe(pd.read_csv(df5, dtype='unicode'))
            except: #xls , not yet finalized
                st.dataframe(pd.read_excel(df5, engine='openpyxl').astype(str))
