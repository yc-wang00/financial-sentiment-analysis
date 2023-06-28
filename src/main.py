import streamlit as st
import pandas as pd
from stock_news_utils import get_stock_news
from iris.sdk import infer

api_key = '649b1d2f4aadf0.76487539'


example = ['Rivian’s Stock Price Rises',
 'Blink Charging Stock Pops Ahead Of Earnings As Infrastructure Bill Earmarks Billions For EV Charging',
 "Explainer-Five legal questions raised by Elon Musk's unorthodox share sales",
 'It’s bizarro world in the auto industry, again',
 'EV Stocks On Fire: Tesla Rival Lucid Rallies, Rivian Extends First-Day Pop, Fisker Breaks Out',
 'Stock Market Today: Dour Disney Results Drag Down the Dow',
 'Elon Musk Is Unloading Billions of Dollars of Tesla Stock',
 'Blink Charging Stock Pops On Record Revenue, But Earnings Miss',
 "If you're worried about a stock market correction, Jim Cramer just mentioned five 'borderline unstoppable' megatrends for the rest of 2021",
 'Dow Jones Lags As Disney Earnings Weigh; Tesla Falls After Elon Musk Does This; Rivian Stock Explodes',
 '6 ProShares ETFs Betting On the Future of Next-Gen Industries',
 'Dow Jones Futures: Rivian Stock Revs Higher In Market Rally; Tesla Digests Elon Musk Sales',
 'Musk Throws Fresh Shade at Rivian a Day After Rival’s Big IPO',
 "Musk says high production, breakeven cash flow 'true test' for Rivian"]

label_map = {"LABEL_0": "negative", "LABEL_1": "neutral", "LABEL_2": "positive"}



# initialize session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if 'news' not in st.session_state:
    st.session_state.news = []

if 'infer_label' not in st.session_state:
    st.session_state.infer_label = []

if 'infer_score' not in st.session_state:
    st.session_state.infer_score = []

def click_button():
    """button for retrieving news"""
    st.session_state.clicked = True

def infer_button():
    """button for inferencing"""
    current_news = st.session_state.news
    res = []
    for text in current_news:
        res.append(infer(url="localhost:8000", task_name="sequence_classification", text=[text])[0])
    print(res)
    for item in res:
        item['label'] = label_map[item['label']]

    st.session_state.infer_label = [r['label'] for r in res]
    st.session_state.infer_score = [r['score'] for r in res]

def clear_button():
    """button for clearing all session state"""
    st.session_state.clicked = False
    st.session_state.news = []
    st.session_state.infer_label = []
    st.session_state.infer_score = []
    
    
st.title('Stock News Sentiment Analysis')
st.write("This app retrieves the latest news for a stock and performs sentiment analysis on the news.")

stock_symbol = st.text_input("Please enter the symbol for a stock (e.g. AAPL for Apple):")
st.write("You entered: ", stock_symbol)
    
col1, col2, col3 = st.columns(3)
col1.button('Retrieve News', on_click=click_button)

if st.session_state.clicked:
    news = get_stock_news(stock_symbol, api_key)
    if not news:
        news = example
        stock_symbol = 'TSLA' # use TSLA as example 
        st.write("__:red[Error retrieving news! We will use example batch from TSLA.]__")
    st.session_state.news = news
    
    st.markdown(f"## News: {stock_symbol}")

    df = pd.DataFrame(columns=['News'])
    df['News'] = news
    df['Score'] = st.session_state.infer_score or [''] * len(news)
    df['Sentiment'] = st.session_state.infer_label or [''] * len(news)
    st.table(df)

    # infer button for inferencing
    col2.button('Analyze News', on_click=infer_button)

    # clear button for clearing all session state
    col3.button("Clear All", on_click=clear_button)    