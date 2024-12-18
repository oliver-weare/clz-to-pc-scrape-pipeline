import requests
from bs4 import BeautifulSoup

from .utils import get_match


class SalesData:
    def __init__(self, comic):
        self.comic = comic
        self.url = self.get_url()

    def get_url(self):
        hyphonated_title = self.comic.title.replace(" ", "-")
        full_hyphonated_string = (
            f"{self.comic.title} {self.comic.issue} {self.comic.release_year}".replace(
                " ", "-"
            )
        )
        return f"https://www.pricecharting.com/game/comic-books-{hyphonated_title}/{full_hyphonated_string}"

    def scrape_sales_data(self, exchange_rate):
        response = requests.get(self.url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            if soup.find(string="returned 0 results") is not None:
                return "no data"

            price_data_table = soup.find("table", id="price_data")

            if price_data_table:
                grade_pricing = {
                    "ungraded": price_data_table.find("td", id="used_price"),
                    "4.0": price_data_table.find("td", id="complete_price"),
                    "6.0": price_data_table.find("td", id="new_price"),
                    "8.0": price_data_table.find("td", id="graded_price"),
                    "9.0+": price_data_table.find("td", id="box_only_price"),
                }

                for grade, content in grade_pricing.items():
                    price_string = self.get_clean_price(content.get_text())

                    if not price_string.strip():
                        grade_pricing[grade] = "no data"
                        continue

                    digits_only = get_match(r"\d+\.\d+", price_string)

                    grade_pricing[grade] = round(float(digits_only) * exchange_rate, 2)

                return grade_pricing

        return {
            "ungraded": "no data",
            "4.0": "no data",
            "6.0": "no data",
            "8.0": "no data",
            "9.0+": "no data",
        }

    def set_sales_data(self, scrape_data):
        self.ungraded_sale = scrape_data["ungraded"]
        self.grade_4_sale = scrape_data["4.0"]
        self.grade_6_sale = scrape_data["6.0"]
        self.grade_8_sale = scrape_data["8.0"]
        self.grade_9_plus_sale = scrape_data["9.0+"]

    def get_clean_price(self, price):
        return price.replace("$", "").replace("-", "")
