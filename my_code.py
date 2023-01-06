import requests

#Insert whatever company stock you want here
stock_name = "TSLA"
company_name = "Tesla Inc"

#get you own API key by logging into alphavantage.co and https://newsapi.org/register
my_API_key = "8FJ0NDXIHSNTIQNL"
news_API_key = "4d8c8827c6734a64be63d2e73697ee73"

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

#get related news
url_2 = "https://newsapi.org/v2/everything?q="+company_name+"&apiKey="+news_API_key
req_2 = requests.get(url_2)
articles = req_2.json()["articles"]

#get first 3 articles 
important_articles = articles[:3]
print(important_articles)
