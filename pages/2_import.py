
'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import time as tm
#from streamlit_multipage import MultiPage


st.markdown("# Import Data ")
#st.sidebar.markdown("# Import Data-")

datatab1, datatab2, datatab3, datatab4, datatab5 = st.tabs(["Dataset 1","Dataset 2", "Dataset 3", "Dataset 4","Dataset 5"])

with datatab1:
    st.markdown('Select your data file')
    dfa1 = st.file_uploader("Choose a file",type=['csv', 'xlsx'], key='df1')
    if dfa1 is not None:
        try:
            df1 = pd.read_csv(dfa1)
        except Exception as e:
            print(e)
            df1 = pd.read_excel(dfa1)
        st.write(df1)

with datatab2:
    st.markdown('Select your data file')
    dfa2 = st.file_uploader("Choose a file", key='df2')
    if dfa2 is not None:
        df2 = pd.read_csv(dfa2)
        st.write(df2)


with datatab3:
    st.markdown('Select your data file')
    dfa3 = st.file_uploader("Choose a file", key='df3')
    if dfa3 is not None:
        df3 = pd.read_csv(dfa3)
        st.write(df3)

with datatab4:
    st.markdown('Select your data file')
    dfa4 = st.file_uploader("Choose a file", key='df4')
    if dfa4 is not None:
        df4 = pd.read_csv(dfa4)
        st.write(df4)

with datatab5:
    st.markdown('Select your data file')
    dfa5 = st.file_uploader("Choose a file", key='df5')
    if dfa5 is not None:
        df5 = pd.read_csv(dfa5)
        st.write(df5)




#********************
# Manage Session State
# *********************
import streamlit.ReportThread as ReportThread
from streamlit.server.Server import Server

def get_session():
    ctx = ReportThread.get_report_ctx().session_id
    this_session = None
    current_session = Server.get_current()._get_session_info(ctx)
    this_session = current_session.session
    # st.write("ch",current_session.session)

    if current_session is None:
        raise RuntimeError(
            "Oh noes. Couldn't get your Streamlit Session object"
            'Are you doing something fancy with threads?')

    return this_session

def get_state(hash_funcs=None):
    session = get_session()
    if not hasattr(session, "_custom_session_state"):
        session._custom_session_state = SessionState(session, hash_funcs)

    return session._custom_session_state

class SessionState:

    def __init__(self, session, hash_funcs):
        """Initialize SessionState instance."""
        self.__dict__["_state"] = {
            "data": {},
            "hash": None,
            "is_rerun": False,
            "session": session,
        }

    def __call__(self, **kwargs):
        """Initialize state data once."""
        for item, value in kwargs.items():
            if item not in self._state["data"]:
                self._state["data"][item] = value

    def __getitem__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)

    def __getattr__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)

    def __setitem__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value

    def __setattr__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value

    def clear(self):
        """Clear session state and request a rerun."""
        self._state["data"].clear()
        self._state["session"].request_rerun()

    def sync(self):
        """Rerun the app with all state values up to date from the beginning to fix rollbacks."""

        # Ensure to rerun only once to avoid infinite loops
        # caused by a constantly changing state value at each run.
        #
        # Example: state.value += 1
        if self._state["is_rerun"]:
            self._state["is_rerun"] = False

        elif self._state["hash"] is not None:
            if self._state["hash"] != self._state["hasher"].to_bytes(self._state["data"], None):
                self._state["is_rerun"] = True
                self._state["session"].request_rerun()

        self._state["hash"] = self._state["hasher"].to_bytes(self._state["data"], None)
