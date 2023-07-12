import streamlit as st
import pandas as pd
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report

st.title('Great app')
file = st.file_uploader("Upload file", type=['csv' 
                                             ,'xlsx'
                                             ,'pickle'])

df = pd.read_csv(file, delimiter=',')
pr = df.profile_report()
st_profile_report(pr)