import requests
from bs4 import BeautifulSoup

from .utils import get_match


def get_exchange_rate_url():
    return (
        "https://www.xe.com/en-gb/currencyconverter/convert/?Amount=1&From=USD&To=GBP"
    )


def scrape_exchange_rate():
    response = requests.get(get_exchange_rate_url())

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        p_tag = soup.find("p", class_="sc-e08d6cef-1 fwpLse")

        if p_tag:
            p_tag_text = p_tag.get_text()
            result = float(get_match(r"\d+\.\d+", p_tag_text))
            return round(result, 2)
