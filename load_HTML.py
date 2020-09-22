# Read HTML from a file
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import csv
import re

FILE_BASE_NAME = 'soup'
FILE_COUNT = 5
BASE_DIR_DATA = 'data/'
AVAILABLE = True

NEW_DB = False


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


def csv_to_db(file_name: str, db_name:str):
    conn = None
    try:
        # read the connection parameters
        params = ({
            'dbname': db_name,
            'user': 'postgres',
            'password': 'postgres',
            'host': 'localhost'})
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.copy_expert(
            """COPY buff_table(autopart_name, autopart_price, autopart_balance) from stdin with delimiter as ',' csv QUOTE '\"' ESCAPE '\"' NULL 'null' """,
            open(file_name))
        # Clearing the file
        open(file_name, 'w').close()
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



def db_tables_create(db_name: str, tabl_name: str, columns: []):
    print(db_name)
    print(list(columns))
    """ create tables in the PostgreSQL database"""
    commands = (
        f"""
        CREATE TABLE IF NOT EXISTS {tabl_name} (
            autopart_id SERIAL PRIMARY KEY,
            autopart_name VARCHAR(255) NOT NULL,
            autopart_price DECIMAL(13,2) NOT NULL,
            autopart_balance INTEGER NOT NULL            
        )
        """,
    )
    conn = None
    try:
        # read the connection parameters
        params = ({
            'dbname': db_name,
            'user': 'postgres',
            'password': 'postgres',
            'host': 'localhost'})
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        print(len(commands))
        for command in commands:
            print(command)
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



def database_create(name: str):
    con = psycopg2.connect(dbname='postgres',
                           user='postgres',
                           host='localhost',
                           password='postgres')

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE

    cur = con.cursor()

    # Use the psycopg2.sql module instead of string concatenation
    # in order to avoid sql injection attacs.
    cur.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier(name))
    )




def file_list_get():
    """ Get files list for view """
    file_list = []
    for n in range(1, FILE_COUNT+1):
        file_list.append(f'{FILE_BASE_NAME}{n}.html')
    return tuple(file_list)


def get_soup(file_name: str):
    """ Open file with Soup data """
    with open(BASE_DIR_DATA + file_name, "rb") as f:
        soup = BeautifulSoup(f.read(), "lxml")
    return soup


def add_objs(file_name: str, product_list: list, is_available: bool = True):
    """ Add objects.Product from file with Soup data
        you can enable availability control"""
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
    csv_list = []
    pos_cnt = 0

    files = file_list_get()
    for file in files:
        pos_cnt += add_objs(file, product_list, AVAILABLE)

    for product in product_list:
        in_stock = re.search(r'\d+', product.in_stock).group()
        csv_list.append([product.name, float(product.price), in_stock])


    print(f'\nВыведено {pos_cnt} позиций.')

    file_name = 'data.csv'
    my_file = open(file_name, 'w', newline='')
    for item in csv_list:
        writer = csv.writer(my_file, quoting=csv.QUOTE_ALL)
        writer.writerow([item[0], item[1], item[2]])
    my_file.close()


    csv_to_db('data.csv', 'tst_base-1')




if __name__ == '__main__':
    if NEW_DB:
        database_create('tst_base-1')
        db_tables_create('tst_base-1', ['id', 'name', 'price', 'balance'])
    main()




