#APP STREAMLIT : (commande : streamlit run XX/dashboard.py depuis le dossier python)
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
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
# Show the financial markers from the API
#-------------------------------------------------------


st.header('‍Financial markers')

            #Calling the API : 

API_url = "http://13.36.215.155/"
json_url = get_response(API_url)
#st.write("## Json {}".format(json_url))
API_data = json_url
st.write('S&P500 front month index futures prices:')
st.write(API_data["S&P500 front month index futures prices"])
st.write('10-year US Treasuries futures prices:')
st.write(API_data["10-year US Treasuries futures prices"])
st.write('US dollar 3-month interest rate:')
st.write(API_data["US dollar 3-month interest rate"])
st.write('US dollar 10-year interest rate:')
st.write(API_data["US dollar 10-year interest rate"])
st.write('VIX Index:')
st.write(API_data["VIX Index"])
#----------------------------------------------------------------
# Load the data
#-----------------------------------------------------------------

# Create a Yahoo Finance ticker objects
stock_SP = yf.Ticker('^SPX')
stock_10y_futures = yf.Ticker('ZNZ23.CBT')
stock_3m_interest = yf.Ticker('^IRX')
stock_10y_interest = yf.Ticker('^TNX')
stock_vix_index = yf.Ticker('^VIX')
        
# Fetch historical data for the stocks
historical_data_SP = stock_SP.history(period='1y')
historical_data_10y_futures = stock_10y_futures.history(period='1y')
historical_data_3m_interest = stock_3m_interest.history(period='1y')
historical_data_10y_interest = stock_10y_interest.history(period='1y')
historical_data_vix_index = stock_vix_index.history(period='1y')

# Extract the closing prices for 1 year
prices_SP = historical_data_SP['Close']
prices_10y_futures = historical_data_10y_futures['Close']
prices_3m_interest = historical_data_3m_interest['Close']
prices_10y_interest = historical_data_10y_interest['Close']
prices_vix_index = historical_data_vix_index['Close']

#----------------------------------------------------------------
# Show the plot for 1 year historical prices for the SP500 index
#-----------------------------------------------------------------

st.header('‍Evolution of the S&P500 front month index futures prices within last year')
fig, ax = plt.subplots()
prices_SP.plot(ax=ax)
plt.ylabel('S&P 500 index')
plt.xlabel('Date')
plt.legend()
st.pyplot(fig)
          
#-----------------------------------------------------------------------------------------
# Show the plot for 1 year historical prices for the 10-year US Treasuries futures prices
#-----------------------------------------------------------------------------------------

st.header('‍Evolution of the 10-year US Treasuries futures prices within last year')
fig, ax = plt.subplots()
prices_10y_futures.plot(ax=ax)
plt.ylabel('10-year US Treasuries futures prices')
plt.xlabel('Date')
plt.legend()
st.pyplot(fig)
                   
#-----------------------------------------------------------------------------------------
# Show the plot for 1 year historical prices for the US dollar 3-month interest rate
#-----------------------------------------------------------------------------------------

st.header('‍Evolution of the US dollar 3-month interest rate within last year')
fig, ax = plt.subplots()
prices_3m_interest.plot(ax=ax)
plt.ylabel('US dollar 3-month interest rate')
plt.xlabel('Date')
plt.legend()
st.pyplot(fig)
          
#-----------------------------------------------------------------------------------------
# Show the plot for 1 year historical prices for the US dollar 10-year interest rate
#-----------------------------------------------------------------------------------------

st.header('‍Evolution of the US dollar 10-year interest rate within last year')
fig, ax = plt.subplots()
prices_10y_interest.plot(ax=ax)
plt.ylabel('US dollar 10-year interest rate')
plt.xlabel('Date')
plt.legend()
st.pyplot(fig)
          
#-----------------------------------------------------------------------------------------
# Show the plot for 1 year historical prices for the VIX Index
#-----------------------------------------------------------------------------------------

st.header('‍Evolution of the VIX Index within last year')
fig, ax = plt.subplots()
prices_vix_index.plot(ax=ax)
plt.ylabel('VIX Index')
plt.xlabel('Date')
plt.legend()
st.pyplot(fig)


#streamlit run streamlit_app.py
