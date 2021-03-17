import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""
# Streamlit and use of pandas to show in the web 

## ploting the airquality data
"""
air_quality = pd.read_csv("air_quality_no2.csv",parse_dates= True,index_col=0)
# air_quality
st.line_chart(air_quality)
'''
# Love the way its working
'''

paris = air_quality['station_paris']
if st.checkbox('Show data'):
    
    st.line_chart(paris)