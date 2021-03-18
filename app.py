import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
st.title('My first app')
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
    #ploting using matplotlip
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(paris)
    st.pyplot(fig)
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)