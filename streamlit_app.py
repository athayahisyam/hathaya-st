# Import relevant libraries

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
import statsmodels.api as sm

st.set_page_config(layout="wide")

# Load dataset

df = pd.read_csv("cm_eu.csv")

st.dataframe(df.head())
