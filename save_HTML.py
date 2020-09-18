import urllib.parse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

base_link = "https://gazzap116.ru/search?query="


def get_page_amount(search_link: str):
    """Find amount pages in HTML site """
    html = urlopen(search_link)
    soup = BeautifulSoup(html, 'html.parser')

    el_pagination = soup.find('div',
                              class_="mse2_pagination cataloge__pagination")
    return len(el_pagination.find_all('a'))


def get_html(find_link: str):
    """ Return HTML data from find_link"""
    r = Request(find_link)
    # r.add_header('Cookie', 'sessionid=13cxrt4uytfc6ijvgeoflmb3u9jmjuhil; csrftoken=jdEKPN8iL62hdaq1hmMuID9DMALiiDIq')
    r.add_header('authority', 'gazzap116.ru')
    r.add_header('cache-control', 'max-age=0')
    r.add_header('upgrade-insecure-requests', '1')
    r.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36')
    r.add_header('sec-fetch-dest', 'document')
    r.add_header('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
    r.add_header('sec-fetch-site', 'same-origin')
    r.add_header('sec-fetch-mode', 'navigate')
    r.add_header('sec-fetch-user', '?1')
    r.add_header('accept-language', 'en-US,en;q=0.9')
    html = urlopen(r)
    return html


def get_page_link(find_link, page_num):
    """ return html page link by page number"""
    if page_num == 1:
        link = find_link
    else:
        link = find_link + '&page=' + str(page_num)
    return link


def page_save(link, page_num):
    """ Save HTML page to file by page number """
    html = get_html(link)
    # Save HTML to a file
    with open(f"soup{page_num}.html", "wb") as f:
        while True:
            chunk = html.read(1024)
            if not chunk:
                break
            f.write(chunk)


def get_search_link():
    """ return url+search request for first HTML pages"""
    find_detail = input('Название детали: ').strip()
    if find_detail == '':
        return 'https://127.0.0.1'
    return base_link + urllib.parse.quote(find_detail)


def main():
    """Download all pages with results by search bar from site www.gazzap116"""
    search_link = get_search_link()
    page_count = get_page_amount(search_link)
    print(f'Количество страниц: {page_count}')

    for page_item in range(1, page_count + 1):
        def_link = get_page_link(search_link, page_item)
        print(def_link)
        page_save(def_link, page_item)


main()
