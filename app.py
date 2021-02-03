import streamlit as st
import pandas as pd

data=pd.read_csv('indian_food.csv')
st.title('Welcome to FoodHut')
st.image('a.jpj')
nav=st.sidebar.selectbox('Go to:',('Home','Recipe Guide','Contribute to our page'))
if nav=='Home':
	st.table(data)
