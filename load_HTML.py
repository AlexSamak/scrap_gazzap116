# Read HTML from a file
from bs4 import BeautifulSoup


with open("soup.html", "rb") as f:
    soup = BeautifulSoup(f.read(), "lxml")

print(soup.title)
# <title>All Cryptocurrencies | CoinMarketCap</title>