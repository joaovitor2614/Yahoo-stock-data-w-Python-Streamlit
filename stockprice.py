import yfinance as yf
import streamlit as st
import pandas as pd
st.write("""
 # Stock Price Data App
 
""")

st.sidebar.header('User input features')
selected_stock = st.sidebar.selectbox('Stock', ['NFLX', 'CSV', 'MSFT'])
selected_period = st.sidebar.selectbox('Período em dias', list(reversed(range(2, 20))))
@st.cache
def load_stock(symbol, period):
    tickerData = yf.Ticker(symbol)
    tickerHistory = tickerData.history(period=f'{period}d')
    pd_history = pd.DataFrame(tickerHistory)
    return pd_history
    

stock_data = load_stock(selected_stock, selected_period)
st.header(f'{selected_stock} on NASDAQ')
st.subheader(f'{selected_period} days period')
st.bar_chart(stock_data)





