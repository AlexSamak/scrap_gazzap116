import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

BASE_LINK = "https://baza.drom.ru/kazan/sell_spare_parts/+/%E2%FB%F5%EB%EE%EF%ED%E0%FF+%F1%E8%F1%F2%E5%EC%E0/model/%E3%E0%E7+%E3%E0%E7%E5%EB%FC/"
BASE_DIR_DATA = 'data/'


def page_save(link, page_num):
    """ Save page from URL link and add to filename page number """
    html = urlopen(link)

    # Save HTML to a file
    with open(f"{BASE_DIR_DATA}soup{page_num}.html", "wb") as f:
        while True:
            chunk = html.read(1024)
            if not chunk:
                break
            f.write(chunk)


def main():
    page_save(BASE_LINK, 48)


main()
