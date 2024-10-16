import streamlit as st
import pandas as pd
import numpy as np


def app():

    st.title('Frontend Tests')
    st.write('This is a test page for the frontend of the app.')
    st.write('The purpose of this page is to test the frontend of the app.')
    st.write('The frontend of the app is built using Streamlit.')

    st.balloons()
    st.success('Frontend tests have passed!')

if __name__ == '__main__':
    app()
