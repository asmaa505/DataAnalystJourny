

import streamlit as st
import pandas as pd

data1 = pd.read_csv('spam_ham_dataset.csv')
st.write( data1)