import streamlit as st
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
# first line 
st.set_page_config(page_title = "Visualization Project" , layout = "centered" , page_icon = ":bar_chart:")
st.title(":bar_chart: Visualization Project")

files = ["House Price India.csv" , "Breast_Cancer.csv" , "Salary_Data.csv" , "Airbnb_dataset.csv"]
select_files = st.selectbox("Select file... " , files , index = None)

if select_files:
    df = pd.read_csv(select_files)
    # col name
    cols = df.columns.tolist()
    
    col1 , col2 = st.columns(2)
    
    
    
    with col1 :
        st.write(" ")
        st.write(df.head())
    with col2 :
        x_axis = st.selectbox("Select X_axis" , cols + ["None"] , index = None)
        y_axis = st.selectbox("Select Y_axis" , cols + ["None"] , index = None)
        charts = ["Line plot" , "Scatter plot" , "Distribution plot" , "Count plot" , "Bar plot"]
        selected_plot = st.selectbox("Select your chart" ,charts + ["None"] , index = None  )
    if st.button("Generate Plot"):
        fig , ax = plt.subplots(figsize = (6,4))
        if selected_plot == "Line plot":
            sns.lineplot(x = df[x_axis] , y = df[y_axis] , estimator = "max" , ax = ax)
        
        elif selected_plot == "Scatter plot":
            sns.scatterplot(x = df[x_axis] , y = df[y_axis] , ax = ax )
        
        elif selected_plot == "Distribution plot":
            sns.histplot(x = df[x_axis] , kde = True , ax = ax)
        
        elif selected_plot == "Count plot":
            sns.countplot(x = df[x_axis] , ax = ax)
        
        elif selected_plot == "Bar plot":
            sns.barplot(x = df[x_axis] , y = df[y_axis] , ax = ax)
        else:
            st.write("Please Select Chart")
        
        
        plt.title(f"{selected_plot} of {x_axis} vs {y_axis}")
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        ax.tick_params(axis = 'x' , labelsize = 10)
        ax.tick_params(axis = 'y' , labelsize = 10)
        
        st.pyplot(fig)
        
        
        