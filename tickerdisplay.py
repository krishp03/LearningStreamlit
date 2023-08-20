import streamlit as st
import yfinance as yf
import pandas as pd
st.write("""
         # My First Streamlit App
         ### Goal: Display Stock Price since 2011
         ##### Note: Does not display trend if invalid ticker is entered
         """)
history = None
while history is None:
    try:
        ticker_symbol = (st.text_input("Ticker Symbol(Please make sure it is all caps)")
                            .strip()
                            .capitalize())
        ticker = yf.Ticker(ticker_symbol)
        history = ticker.history(start= '2011-1-1')
    except:
        history = None
    

st.line_chart(history.Close)
