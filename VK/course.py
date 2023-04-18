import requests
from bs4 import BeautifulSoup
from datetime import datetime
url = "http://www.cbr.ru/scripts/XML_daily.asp?"
today = datetime.today()
today = today.strftime("%d/%m/%Y")
payload = {"date_req": today}

response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, 'html.parser')

def get_course(currency):
    global i
    if currency == 'доллар':
        i = 'R01235'
    elif currency == 'евро':
        i = 'R01239'
    try:
        return str(xml.find("valute", {'id': i}).value.text)
    except:
        return f"не удалось найти информацию"
