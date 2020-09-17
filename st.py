import urllib.parse


site = 'search?query=%D0%B1%D0%B5%D0%BD%D0%B7%D0%BE%D0%BD%D0%B0%D1%81%D0%BE%D1%81'

view = urllib.parse.unquote(site)

print(view)

#
# <div class="mse2_pagination cataloge__pagination">
#     <a href="search?query=%D0%B1%D0%B5%D0%BD%D0%B7%D0%BE%D0%BD%D0%B0%D1%81%D0%BE%D1%81" class="c__pag__link active">1</a><a href="search?page=2&amp;query=%D0%B1%D0%B5%D0%BD%D0%B7%D0%BE%D0%BD%D0%B0%D1%81%D0%BE%D1%81" class="c__pag__link">2</a><a href="search?page=3&amp;query=%D0%B1%D0%B5%D0%BD%D0%B7%D0%BE%D0%BD%D0%B0%D1%81%D0%BE%D1%81" class="c__pag__link">3</a>
# </div>