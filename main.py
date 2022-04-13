import datetime
import time
from bs4 import BeautifulSoup
import requests

URL = "https://www.marketwatch.com/investing/index/spx"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/99.0.4844.51 Safari/537.36"}

def get_price():
    doc = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(doc.content, "html.parser")
    price_extraction = soup.find('div', {'class': 'intraday__data'})
    price_str = (price_extraction.find('bg-quote', {'class': 'value'}).get_text()).replace(",", "")
    # print(price)
    return price_str


def get_date():
    date_and_time = datetime.datetime.now()
    date_and_time = date_and_time.strftime("%Y-%m-%d %H:%M:%S")
    # print(date_and_time)
    date_and_time = date_and_time.replace(" ", "-")
    return date_and_time.replace(":", "-")


if __name__ == "__main__":

    while True:
        try:
            price = get_price()
        except:
            continue
        date = get_date()
        with open("S&P500_VALUE.txt", 'a') as f:
            f.write('%s %s\n' % (date, price))
        f.close()
        time.sleep(5)