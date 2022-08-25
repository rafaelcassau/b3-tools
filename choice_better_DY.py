import re
import requests
from decimal import Decimal
from bs4 import BeautifulSoup


FIIS_LIST = [
    ("BCFF11", "FOF"),
    ("KNCR11", "CRI"),
    ("KNRI11", "Laje/Logistica"),
    ("XPLG11", "Logistica"),
    ("VISC11", "Shopping"),
    ("VRTA11", "CRI"),
    ("MXRF11", "CRI"),
    ("XPML11", "Shopping"),
    ("VILG11", "Logistica"),
    ("ALZR11", "Laje/Logistica"),
    ("IRDM11", "CRI"),
    ("PVBI11", "Laje comercial"),
    ("BTLG11", "Logistica"),
    ("HGLG11", "Logistica"),
    ("HGRU11", "Renda Urbana"),
]

URL_PREFIX = "https://www.fundsexplorer.com.br/funds/{}"


def scrapy_fiis_price(fiis_list):
    fiis_data_list = []

    for fii, kind in fiis_list:
        url = URL_PREFIX.format(fii)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        price_soup = soup.select(".price")
        indicator_soup = soup.select(".indicator-value")
        
        data = {
            "fii": fii,
            "kind": kind,
            "indicators": {
                "market_value": to_decimal(price_soup[0].text),
                "equity_value": to_decimal(indicator_soup[4].text),
                "last_yield": to_decimal(indicator_soup[1].text),
                "dividend_yield": to_decimal(indicator_soup[2].text),
                "P/VP": to_decimal(indicator_soup[6].text),
            }
        }
        fiis_data_list.append(data)

    return fiis_data_list


def to_decimal(value):
    value = re.sub("[a-zA-Z]|[$%]|\s", "", value)
    value = re.sub(",", ".", value)
    return Decimal(value)


def build_fiis_list(money, fiis_list):
    fiis_new_list = []
    for fii in fiis_list:
        kind = fii["kind"]
        market_value = fii["indicators"]["market_value"]
        equity_value = fii["indicators"]["equity_value"]
        last_yield = fii["indicators"]["last_yield"]
        quotas_amount = money // market_value
        change = money % market_value
        next_payment_yield_BRL = quotas_amount * last_yield
        fiis_new_list.append({
            "fii": fii["fii"],
            "kind": kind,
            "quotas_amount": quotas_amount,
            "next_payment_yield_BRL": next_payment_yield_BRL,
            "change": change,
            "equity_value": equity_value,
            "market_value": market_value,
            "P/VP": fii["indicators"]["P/VP"]
        })
    return fiis_new_list


def ordering_fiis_by(fiis_list, order_by, reverse=False):
    return sorted(fiis_list, key=lambda fii: fii[order_by], reverse=reverse)


def print_fiis(fiis_list):
    for fii in fiis_list:
        print("\n************************")
        print(f"|FII: {fii['fii']} | Tipo: {fii['kind']}|")
        print("************************")
        print(f"Next Payment: {fii['next_payment_yield_BRL']}")
        print(f"Quotas amount: {fii['quotas_amount']}")
        print(f"change: {fii['change']}")
        print(f"equity_value: {fii['equity_value']}")
        print(f"market_value: {fii['market_value']}")
        print(f"P/VP: {fii['P/VP']}")


if __name__ == "__main__":
    money = Decimal(input("informe o valor do aporte em R$: "))

    fiis_data_list = scrapy_fiis_price(FIIS_LIST)
    fiis = build_fiis_list(money, fiis_data_list)

    #ordered_fiis = ordering_fiis_by(fiis, "next_payment_yield_BRL", reverse=True)
    ordered_fiis = ordering_fiis_by(fiis, "P/VP", reverse=False)

    print_fiis(ordered_fiis)



    
