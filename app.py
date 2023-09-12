#APP STREAMLIT : (commande : streamlit run XX/dashboard.py depuis le dossier python)
import streamlit as st
import numpy as np
import pandas as pd
#import time
import math
from urllib.request import urlopen
import json
import requests
import warnings
warnings.filterwarnings("ignore")


def get_response(url):
    response = requests.get(url)
    print(response)
    return response.json()


with st.sidebar:
 st.header("💰 Forecast")
 st.write("## Actions")
 SP500_futures = st.checkbox("View S&P500 index futures")
 interest_rate = st.checkbox("View 10 year interest rate")   
 vix_index = st.checkbox("View VIX index")
    
            
    #######################################
    # HOME PAGE - MAIN CONTENT
    #######################################

    #Titre principal

html_temp = """
    <div style="background-color: gray; padding:10px; border-radius:10px">
    <h1 style="color: white; text-align:center">Dashboard - Forecasting</h1>
    </div>
    <p style="font-size: 20px; font-weight: bold; text-align:center">
    Finance</p>
    """
st.markdown(html_temp, unsafe_allow_html=True)

with st.expander("What is this app for?"):
        st.write("This app is used to forcast the financial markers") 


    
#-------------------------------------------------------
# Show the S&P500 index futures
#-------------------------------------------------------

if (SP500_futures):
    st.header('‍S&P500 index futures')

            #Calling the API : 

    API_url = "https://app0709-lemishkotetiana.b4a.run/"
    json_url = get_response(API_url)
    #st.write("## Json {}".format(json_url))
    API_data = json_url["forecasted_SP_index"]
    st.write(API_data)
    
#-------------------------------------------------------
# Show the 10 year interest rate
#-------------------------------------------------------

if (interest_rate):
    st.header('‍10 year interest rate')

            #Calling the API : 

    API_url = "model1209-lemishkotetiana.b4a.run/"
    json_url = get_response(API_url)
    #st.write("## Json {}".format(json_url))
    API_data = json_url["forecasted_10y_interest"]
    st.write(API_data)
    
#-------------------------------------------------------
# Show the VIX index
#-------------------------------------------------------

if (vix_index):
    st.header('‍10 year interest rate')

            #Calling the API : 

    API_url = "model1209-lemishkotetiana.b4a.run/"
    json_url = get_response(API_url)
    #st.write("## Json {}".format(json_url))
    API_data = json_url["forecasted_vix_index"]
    st.write(API_data)    
    
#streamlit run streamlit_app.py