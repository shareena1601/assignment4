#import libraries

import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import matplotlib
#matplotlib.use('Agg')

import seaborn as sns 
import streamlit as st #for using streamlit

#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Assignment 4 healthcare-dataset-stroke-data")

# Header
st.header("Icfoss")

# Subheader
st.subheader("Language&Technology")

# Text
st.text("Assignment 4 shareena a")

# Markdown
st.markdown("## stroke data set using Streamlit  ")

#import dataset
df = pd.read_csv('healthcare-dataset-stroke-data.csv')

#First 10 rows
df10 = df.head(10)

#Display the table
st.table(df10)

#pipenv install seaborn matplotlib, in ubuntu


#pairplot
st.subheader("Pairplot")
sns.pairplot(df10 ,hue='gender',palette='rainbow')
st.pyplot()

#bar plot
st.subheader("Bar Plot")
df10.plot(kind='bar')
st.pyplot()

#Displot
st.subheader("Displot")
sns.displot(df10['bmi'])
st.pyplot()

#joinplot
st.subheader("JointPlot")
sns.jointplot(x='bmi',y='avg_glucose_level',data=df10 ,kind='scatter')
st.pyplot()

#Rugplot
st.subheader("Rugplot")
sns.rugplot(df10['avg_glucose_level'])
st.pyplot()


#Correation
st.subheader("Heatmap")
sns.heatmap(df10.corr(),cmap='coolwarm',annot=True)
st.pyplot()
