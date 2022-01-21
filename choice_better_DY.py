import re
import requests
from decimal import Decimal
from bs4 import BeautifulSoup


FIIS_LIST = [
    "BCFF11",
    "KNCR11",
    "KNRI11",
    "XPLG11",
    "VISC11",
    "XPPR11",
    "VRTA11",
    "MXRF11",
    "XPML11",
    "VILG11",
    "ALZR11",
    "IRDM11",
    "PVBI11",
]

URL_PREFIX = "https://www.fundsexplorer.com.br/funds/{}"


def scrapy_fiis_price(fiis_list):
    fiis_data_list = []

    for fii in fiis_list:
        url = URL_PREFIX.format(fii)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        soup = soup.select(".indicator-value")
        
        data = {
            "fii": fii,
            "indicators": {
                "last_yield": to_decimal(soup[1].text),
                "dividend_yield": to_decimal(soup[2].text),
                "equity_value": to_decimal(soup[4].text),
                "P/VP": to_decimal(soup[6].text),
            }
        }
        fiis_data_list.append(data)

    return fiis_data_list


def to_decimal(value):
    value = re.sub("[a-zA-Z]|[$%]|\s", "", value)
    value = re.sub(",", ".", value)
    return Decimal(value)


def find_most_high_yield_return_based_on_last_payment(money, fiis_list):
    next_payment_yield_list = []
    for fii in fiis_list:
        equity_value = fii["indicators"]["equity_value"]
        last_yield = fii["indicators"]["last_yield"]
        quotas_amount = money // equity_value
        next_payment_yield_BRL = quotas_amount * last_yield
        next_payment_yield_list.append({"fii": fii["fii"], "next_payment_yield_BRL": next_payment_yield_BRL})  

    return sorted(next_payment_yield_list, key=lambda fii: fii["next_payment_yield_BRL"], reverse=True)


def print_fiis(fiis_list):
    for fii in fiis_list:
        print(fii)


if __name__ == "__main__":
    fiis_data_list = scrapy_fiis_price(FIIS_LIST)

    money = Decimal(input("informe o valor do aporte em R$: "))

    next_payment_yield_list = find_most_high_yield_return_based_on_last_payment(money, fiis_data_list)
    print_fiis(next_payment_yield_list)



    
