import urllib.parse
from urllib.request import urlopen


def main():
    find_detail = input('Название детали: ').strip()
    if find_detail == '':
        return
    url = "https://gazzap116.ru/search?query=" + urllib.parse.quote(
        find_detail)

    html = urlopen(url)

    # Save HTML to a file
    with open("soup.html", "wb") as f:
        while True:
            chunk = html.read(1024)
            if not chunk:
                break
            f.write(chunk)









main()