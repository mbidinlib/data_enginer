
'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''
from io import StringIO
import pandas as pd
import streamlit as st

#Installed programs
#pip install streamlit-multipage

#Add background color
body_format = '''
<style>
    body {
        background-color: brown;
        secondary-background-color:red;
        }
    h1 {
        color: maroon;
        font-family: Tahoma;
        font-size: 200%;
    }
    h2 {
        color: #BA4A00;
        font-family: open sans;
    }
    h3 {
        color: #045106;
        font-family: oopen sans;
    }
    p {
        font-family: open sans;
    }    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    </body>

    '''
st.markdown(body_format, unsafe_allow_html=True)


#st.sidebar.markdown("# Home page")
with st.sidebar.container():
    st.image('picture.jpg',
    caption='Mathew Bidinlib', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    #st.image(image, width= use_column_width=True)

st.markdown("# MGlory Data Engineering Toolkit ")

st.markdown("""
    Welcome to MGlory Data Engineering toolkit.
    This is a python based tool that would help you prepare your dataset for analysis.
    The tool contains the following components""")

hcol1, hcol2 = st.columns(2)

with hcol1:
    st.markdown("<h4><u>Import Page</u></h4>",unsafe_allow_html=True)
    exp1 = st.expander("Help note",expanded=True)
    exp1.write('''
    This page is the starting point where you would be able to import upto five (5) datasets for your work.
    Each dataset is in a seperate tab and you can navigate across tabs
    ''')
with hcol2:
    st.markdown("<h4><u>Duplicates Page/u></h4>",unsafe_allow_html=True)
    exp2 = st.expander("Help note",expanded=True)
    exp2.write(''''
    This page is would help you check for duplicates in the imported datasets using some key variables 
    and also remove duplicates if there are any
    ''')
with hcol1:
    st.markdown("<h4><u>Outliers Page</u></h4>",unsafe_allow_html=True)
    exp3 = st.expander("Check help note",expanded=True)
    exp3.write(''''
    This page is would help you check for outliers in your importd dataset
    ''')

with hcol2:
    st.markdown("<h4><u>Merge Page</u></h4>",unsafe_allow_html=True)
    exp4 = st.expander("Check help note",expanded=True)
    exp4.write(''''
    This would help you to merge selected datasets that you imported into one. 
    You may also append datasets if needed
    ''')


# Set the footer
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.github.com/mbidinlib/" target="_blank">Mathew Bidinlib </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
