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

#yesterdays closing price 
yest_close_price = info_list[0]["4. close"]

#before yesterdays closing price
before_yesterday = info_list[1]["4. close"]

# %difference  = |new-old|/old
perc_difference = abs(float(before_yesterday)-float(yest_close_price))/ float(before_yesterday)*100
rounded_perc_difference = round(perc_difference,2)
print(rounded_perc_difference)