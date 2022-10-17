from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import tabula

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

uploaded_file = st.file_uploader('Upload pdf file:')
if uploaded_file is not None:
    df = tabula.read_pdf(uploaded_file, pages="all", )
    df.to_excel('df_test.xlsx')

st.download_button(label='📥 Download Current Result',
                                data=df)
