from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests_):
    response = requests_.get(
        f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}').content
    soup = BeautifulSoup(response, "lxml")
    if cur_from == 'RUR':
        value1 = 1
        nominal1 = 1
    else:
        value1 = soup.find('charcode', text=cur_from).find_next_sibling(
            'value').text
        value1 = Decimal(value1.replace(',', '.'))
        nominal1 = soup.find('charcode', text=cur_from).find_next_sibling(
            'nominal').string
        nominal1 = Decimal(nominal1)
    if cur_to == 'RUR':
        value2 = 1
        nominal2 = 1
    else:
        value2 = soup.find('charcode', text=cur_to).find_next_sibling(
            'value').string
        value2 = Decimal(value2.replace(',', '.'))
        nominal2 = soup.find('charcode', text=cur_to).find_next_sibling(
            'nominal').string
        nominal2 = Decimal(nominal2)
    res = (((amount / nominal1) * value1) / value2) * nominal2
    result = res.quantize(Decimal("1.0000"))
    return result
