import urllib.parse

"""" encode to URL string"""
find_detail = 'глушитель'
start = "https://gazzap116.ru/search?query=" + urllib.parse.quote(find_detail)
print(start)
print("https://gazzap116.ru/search?query=%D0%B3%D0%BB%D1%83%D1%88%D0%B8%D1%82%D0%B5%D0%BB%D1%8C")


print('\n\n')
""" decode to UTF8"""
site = 'https://detaligaz16.ru/page/4/?s=%D0%B0%D0%BC%D0%BE%D1%80%D1%82%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80&post_type=product'
view = urllib.parse.unquote(site)
print(view)


print('\n\n')
""" decode to Windows CP1251"""
site = 'https://baza.drom.ru/kazan/sell_spare_parts/+/%E2%FB%F5%EB%EE%EF%ED%E0%FF+%F1%E8%F1%F2%E5%EC%E0/model/%E3%E0%E7+%E3%E0%E7%E5%EB%FC/'
site = site.replace('^', '')
view = urllib.parse.unquote_to_bytes(site).decode('cp1251')
print(view)

