#create streamlit app

import streamlit as st
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


#load data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

#set title
st.title('Apple Stock Price')

#set subheader
st.subheader('Apple Stock Price Data')

#show data
st.write(df)

#show data as chart
st.line_chart(df.Close)
st.line_chart(df.High)
st.line_chart(df.Low)

#show data as table
st.table(df)

