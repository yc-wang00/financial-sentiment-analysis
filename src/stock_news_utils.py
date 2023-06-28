import requests


def get_stock_news(stock, api_key, num_news=10) -> list:
    """get the latest news for a stock from EOD Historical Data

    Args:
        stock (str): stock symbol
        api_key (str): EOD Historical Data API key
        num_news (int, optional): number of new to retrieve. Defaults to 10.

    Returns:
        list(str): a list of news titles
    """
    url = f"https://eodhistoricaldata.com/api/news?api_token={api_key}&s={stock}"
    try:
        news_json = requests.get(url).json()
        return [news_json[-i]["title"] for i in range(num_news)]
    except Exception:
        print("Error retrieving news")
        return []


def get_customized_news(stock, start_date, end_date, n_news, api_key, offset=0) -> list:
    url = f"https://eodhistoricaldata.com/api/news?api_token={api_key}&s={stock}&limit={n_news}&offset={offset}&from={start_date}&to={end_date}"
    try:
        news_json = requests.get(url).json()
        return [news_json[-i]["title"] for i in range(len(news_json))]

    except Exception:
        print("Error retrieving news")
        return []
