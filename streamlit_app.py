from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
import tabula
from tabula import read_pdf

"""
# Hertz pdf to excel converter
Specifically designed for AutoSweep RFID pdf.
"""

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data

uploaded_file = st.file_uploader('Upload pdf file:')
if uploaded_file is not None:
    dfs = tabula.read_pdf(uploaded_file, pages="all", pandas_options={'header': None}, relative_area = True, area = [17,0,80,100])
    new_df = pd.concat(dfs)
    df_xlsx = to_excel(new_df)
    st.download_button(label='📥 Download Excel version',
                            data=df_xlsx,file_name=uploaded_file.name+'.xlsx')
