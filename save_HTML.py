import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

base_link = "https://gazzap116.ru/search?query="


def get_page_amount(search_link):
    """Find in HTML site amount pages"""
    html = urlopen(search_link)
    soup = BeautifulSoup(html, 'html.parser')

    el_pagination = soup.find('div',
                              class_="mse2_pagination cataloge__pagination")
    return len(el_pagination.find_all('a'))


def get_html(find_link):
    html = urlopen(find_link)


def get_page_link(find_link, page_num):
    """ return html from page number"""
    if page_num == 1:
        link = find_link
    else:
        link = find_link + '&page=' + str(page_num)
    return link


def page_save(link, page_num):
    html = urlopen(link)

    # Save HTML to a file
    with open(f"soup{page_num}.html", "wb") as f:
        while True:
            chunk = html.read(1024)
            if not chunk:
                break
            f.write(chunk)


def get_search_link():
    """ return url for first request"""
    find_detail = input('Название детали: ').strip()
    if find_detail == '':
        return 'https://127.0.0.1'
    return base_link + urllib.parse.quote(find_detail)


def main():
    search_link = get_search_link()
    page_count = get_page_amount(search_link)
    print(f'Количество страниц: {page_count}')

    for page_item in range(1, page_count + 1):
        def_link = get_page_link(search_link, page_item)
        print(def_link)
        page_save(def_link, page_item)


main()
