import requests

#Insert whatever company stock you want here
stock_name = "TSLA"

#get you own API key by logging into alphavantage.co
my_API_key = "8FJ0NDXIHSNTIQNL"

#endpoint provided in the documentation 
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=" + stock_name + "&apikey=" + my_API_key
req = requests.get(url)
information = req.json()["Time Series (Daily)"]
info_list = [value for (key,value) in information.items()]