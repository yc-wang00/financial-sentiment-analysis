import streamlit as st
import pandas as pd
import requests
from iris.sdk import infer

api_key = '649b1d2f4aadf0.76487539'

def get_stock_news(stock, api_key):
    url = f'https://eodhistoricaldata.com/api/news?api_token={api_key}&s={stock}'
    news_json = requests.get(url).json()
    
    news = []
    
    for i in range(10):
        title = news_json[-i]['title']
        news.append(title)
    
    return news


def get_customized_news(stock, start_date, end_date, n_news, api_key, offset = 0):
    url = f'https://eodhistoricaldata.com/api/news?api_token={api_key}&s={stock}&limit={n_news}&offset={offset}&from={start_date}&to={end_date}'
    news_json = requests.get(url).json()
    
    news = []
    
    for i in range(len(news_json)):
        title = news_json[-i]['title']
        news.append(title)
    
    return news



st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")

stock_symbol = st.text_input("Please enter the symbol for a stock (e.g. AAPL for Apple):")
st.write("You entered: ", stock_symbol)

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Get News', on_click=click_button)


if 'news' not in st.session_state:
    st.session_state.news = []

if st.session_state.clicked:
    try:
        news = get_stock_news(stock_symbol, api_key)
    except Exception as e:
        news = ['Invalid stock symbol', 'Please try again', 'e.g. AAPL for Apple']
    
    st.session_state.news = news
    st.write(news)
    

    
res = []
if st.button("Analyze"):
    current_news = st.session_state.news
    if current_news is not None:
        for text in current_news:
            res.append(infer(url="localhost:32769", task_name="sequence_classification", text=[text]))
            
        st.write(res)