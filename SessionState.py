import streamlit as st

class SessionState:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def state(self):
        return st.session_state

    def __getattr__(self, item):
        return getattr(self.state, item, None)

    def __setattr__(self, key, value):
        setattr(self.state, key, value)
