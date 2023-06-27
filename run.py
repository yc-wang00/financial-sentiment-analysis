


import requests
api_key = '649b1d2f4aadf0.76487539'

def get_stock_news(stock, api_key):
    url = f'https://eodhistoricaldata.com/api/news?api_token={api_key}&s={stock}'
    news_json = requests.get(url).json()
    
    news = []
    
    for i in range(10):
        title = news_json[-i]['title']
        news.append(title)
    
    return news

amzn_news = get_stock_news('AMZN', api_key)

def get_customized_news(stock, start_date, end_date, n_news, api_key, offset = 0):
    url = f'https://eodhistoricaldata.com/api/news?api_token={api_key}&s={stock}&limit={n_news}&offset={offset}&from={start_date}&to={end_date}'
    news_json = requests.get(url).json()
    
    news = []
    
    for i in range(len(news_json)):
        title = news_json[-i]['title']
        news.append(title)
    
    return news

tsla_news = get_customized_news('TSLA', '2021-11-09', '2021-11-11', 15, api_key, 0)

print(tsla_news)
print(amzn_news)