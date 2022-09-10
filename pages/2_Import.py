
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
            ds1_name = st.text_input("Short name of your dataset (optional). Default is *dataset1*", key="name1")
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

            if file_ext1 == 'csv':
               dataset_1 = pd.read_csv(StringIO(df1),dtype='unicode')
               st.dataframe(dataset_1) 
                #st.dataframe(pd.read_csv(StringIO(df1),dtype='unicode')) ### Remove  
               st.session_state["dataset1"] = dataset_1                         
            elif file_ext1 == 'xls'or file_ext1 == 'xlsx':
                dataset_1 = pd.read_excel(df1, engine='openpyxl').astype(str)
                st.dataframe(dataset_1)
                st.session_state["dataset1"] = dataset_1
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
            ds2_name = st.text_input("Short name of your dataset (optional). The default is *dataset2*", key="name2")
            if ds2_name:
                st.session_state["ds2_name"] = ds2_name
            if 'ds2_name' in st.session_state:
                #st.write(st.session_state["ds2_name"])
                st.markdown(st.session_state["ds2_name"])            
      
    #Column two 
    with col2:
        if "ds2" in st.session_state:
            st.header("Data overview")  # Give it a header
            df2= st.session_state["ds2"]
            file_ext2 = df2.name.split('.')[-1]  # get file extension of selected file

            if file_ext2 == 'csv':
               dataset_2 = pd.read_csv(df2)
               st.dataframe(dataset_2) 
               st.session_state["dataset2"] = dataset_2
            elif file_ext2 == 'xls'or file_ext2 == 'xlsx': #xls , not yet finalized
                dataset_2 = pd.read_excel(df2, engine='openpyxl').astype(str)
                st.dataframe(dataset_2)
                st.session_state["dataset2"] = dataset_2
            else:
                st.markdown("""**This file is type is currently not accepted. Upload a file with a .csv or xls extenssion. 
                #Support for Other file extensions would be added later**""")

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
            file_ext3 = df3.name.split('.')[-1]  # get file extension of selected file

            if file_ext3 == 'csv':
               dataset_3 = pd.read_csv(df3)
               st.dataframe(dataset_3) 
               st.session_state["dataset3"] = dataset_3
            elif file_ext3 == 'xls'or file_ext3 == 'xlsx': #xls , not yet finalized
                dataset_3 = pd.read_excel(df3, engine='openpyxl').astype(str)
                st.dataframe(dataset_3)
                st.session_state["dataset3"] = dataset_3
            else:
                st.markdown("""**This file is type is currently not accepted. Upload a file with a .csv or xls extenssion. 
                #Support for Other file extensions would be added later**""")


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
            file_ext4 = df4.name.split('.')[-1]  # get file extension of selected file

            if file_ext4 == 'csv':
               dataset_4 = pd.read_csv(df4)
               st.dataframe(dataset_4) 
               st.session_state["dataset4"] = dataset_4
            elif file_ext4 == 'xls'or file_ext4 == 'xlsx': #xls , not yet finalized
                dataset_4 = pd.read_excel(df4, engine='openpyxl').astype(str)
                st.dataframe(dataset_4)
                st.session_state["dataset4"] = dataset_4
            else:
                st.markdown("""**This file is type is currently not accepted. Upload a file with a .csv or xls extenssion. 
                #Support for Other file extensions would be added later**""")

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
            file_ext5 = df5.name.split('.')[-1]  # get file extension of selected file

            if file_ext5 == 'csv':
               dataset_5 = pd.read_csv(df5)
               st.dataframe(dataset_5) 
               st.session_state["dataset5"] = dataset_5
            elif file_ext5 == 'xls'or file_ext5 == 'xlsx': #xls , not yet finalized
                dataset_5 = pd.read_excel(df5, engine='openpyxl').astype(str)
                st.dataframe(dataset_5)
                st.session_state["dataset5"] = dataset_5
            else:
                st.markdown("""**This file is type is currently not accepted. Upload a file with a .csv or xls extenssion. 
                #Support for Other file extensions would be added later**""")