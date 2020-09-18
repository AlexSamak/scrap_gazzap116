import pickle
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

url = "https://stackoverflow.com/questions/52973700/how-to-save-the-beautifulsoup-object-to-a-file-and-then-read-from-it-as-beautifu"
html = urlopen(url)
soup = BeautifulSoup(html,"lxml")

sys.setrecursionlimit(8000)

# Save the soup object to a file
with open("soup.pickle", "wb") as f:
    pickle.dump(soup, f)

# Read the soup object from a file
with open("soup.pickle", "rb") as f:
    soup_obj = pickle.load(f)

print(soup_obj.title)
