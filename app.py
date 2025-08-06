import streamlit as st
from indicators import generate_signals
from telegram_alerts import send_telegram_alert
import pandas as pd
import plotly.graph_objs as go

st.set_page_config(page_title="BTC/ETH Signal Dashboard", layout="wide")
st.title("📈 BTC/ETH Signal Dashboard")

symbol = st.selectbox("Select Symbol", ["BTC-USD", "ETH-USD"])

df = generate_signals(symbol)
st.plotly_chart(go.Figure(data=[go.Candlestick(
    x=df.index,
    open=df['Open'], high=df['High'],
    low=df['Low'], close=df['Close']
)]), use_container_width=True)

if st.button("Send Alert"):
    send_telegram_alert(f"Signal triggered for {symbol}")