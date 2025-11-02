import streamlit as st      
import pandas as pd          
import numpy as np            
 
# Function to load CSV data
def load_data(nrows):
    data = pd.read_csv('directory.csv', nrows=nrows)  # Fixed double pd.read_csv
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data
 
# Display a loading message
data_load_state = st.text('Loading data...')
 
# Load 10,000 rows of data
data = load_data(10000)
 
# Notify that loading is complete
data_load_state.text('Done! (Using st.cache_data)')
 
# Display the raw data
st.subheader('Raw Data')
st.write(data)

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)



from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((1000, 2)) / [50, 50] + [37.76, -122.4],
    columns=["latitude", "longitude"],
)

st.map(df)

from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((60, 3)), columns=["country", "brand"])

chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="country", y="brand", size="brand", color="country", tooltip=["country", "brand"])
)

st.altair_chart(chart)