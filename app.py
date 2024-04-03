import streamlit as st

st.title('My First Streamlit App')

st.write('Hello, world!')

st.header('This is a header')

import pandas as pd
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35]})
st.write(df)