# Read HTML from a file
from bs4 import BeautifulSoup

file_list = (
    'soup1.html', 'soup2.html', 'soup3.html', 'soup4.html', 'soup5.html',)


class Product:
    name = str
    price = str
    in_stock = str
    link = str

    def __init__(self, name, price, in_stock, link):
        self.name = name
        self.price = price
        self.in_stock = in_stock
        self.link = link

    def __repr__(self):
        return str(self.__dict__)


def get_soup(file_name):
    with open(file_name, "rb") as f:
        soup = BeautifulSoup(f.read(), "lxml")
    return soup


def add_objs(file_name: str, product_list: list, is_available: bool = True):
    cnt = 0
    soup = get_soup(file_name)

    for element in soup.find_all('div',
                                 class_="ms2_product cataloge__item_add"):
        name = element.find('h3',
                            class_="cataloge__title cataloge__title_add"). \
            text.strip()
        price = element.find('span', class_="c__price").text.strip()
        in_stock = element.find('p', class_="in_store__line").text.strip()
        link = ""

        if in_stock.find('В наличии') >= 0 or not is_available:
            product = Product(name, price, in_stock, link)
            product_list.append(product)
            cnt += 1
    return cnt


def main():
    product_list = []

    for file in file_list:
        print(add_objs(file, product_list, False))

    for product in product_list:
        print(product.__repr__())


main()