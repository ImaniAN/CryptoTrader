import re
import urllib.request
response = urllib.request.urlopen('https://www.tradingview.com/crypto-screener/')
html = response.read()
text = html.decode()
print(text)