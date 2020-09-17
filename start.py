import requests
from bs4 import BeautifulSoup


class Product:
    name = str
    price = str
    in_stock = str
    count = str

    def __init__(self, name, price, in_stock, count):
        self.name = name
        self.price = price
        self.in_stock = in_stock
        self.count = count

    def __repr__(self):
        return str(self.__dict__)


def main():
    headers = {
        'authority': 'gazzap116.ru',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        'sec-fetch-dest': 'document',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'accept-language': 'en-US,en;q=0.9',
    }

    session = requests.session()

    response = session.get(
        "https://gazzap116.ru/search?query=%D0%B3%D0%BB%D1%83%D1%88%D0%B8%D1%82%D0%B5%D0%BB%D1%8C&page=2",
        headers=headers)

    if response.status_code == 200:
        print("Success")
    else:
        print("Bad result")

    soup = BeautifulSoup(response.text, 'html.parser')

    element = soup.find('div', class_="mse2_pagination cataloge__pagination")
    print(len(element.find_all('a')))

    for element in soup.find_all('div',
                                 class_="ms2_product cataloge__item_add"):
        name = element.find('h3',
                            class_="cataloge__title cataloge__title_add").text.strip()
        price = element.find('span', class_="c__price").text.strip()
        in_stock = element.find('p', class_="in_store__line").text.strip()
        #count = "https://gazzap116.ru/" + element.find('a').get('href')
        count = ""

        product = Product(name, price, in_stock, count)

        print(product.__repr__())


main()
#
# <div class="mse2_pagination cataloge__pagination">
#     <a href="search?query=%D0%B1%D0%B5%D0%BD%D0%B7%D0%BE%D0%BD%D0%B0%D1%81%D0%BE%D1%81" class="c__pag__link active">1</a><a href="search?page=2&amp;query=%D0%B1%D0%B5%D0%BD%D0%B7%D0%BE%D0%BD%D0%B0%D1%81%D0%BE%D1%81" class="c__pag__link">2</a><a href="search?page=3&amp;query=%D0%B1%D0%B5%D0%BD%D0%B7%D0%BE%D0%BD%D0%B0%D1%81%D0%BE%D1%81" class="c__pag__link">3</a>
# </div>
