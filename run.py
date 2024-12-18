from lib.files import delete_file_if_exists, get_csv_data, write_csv_file

from lib.comic import Comic
from lib.sales import SalesData

from lib.paths import INPUT_FILE_PATH, OUTPUT_FILE_PATH

from lib.rate import scrape_exchange_rate

file_data = get_csv_data(INPUT_FILE_PATH)

usd_to_gbp_exchange_rate = scrape_exchange_rate()
comics = [
    [
        "title",
        "issue",
        "release_year",
        "ungraded_sales",
        "4.0_sales",
        "6.0_sales",
        "8.0_sales",
        "9.0+_sales",
    ]
]

for row in file_data:
    this_comic = Comic(row[0], row[1], row[4])
    this_sales_data = SalesData(this_comic)
    this_sales_data.set_sales_data(
        this_sales_data.scrape_sales_data(usd_to_gbp_exchange_rate)
    )

    print(this_comic.title)

    comics.append(
        [
            this_comic.title,
            this_comic.issue,
            this_comic.release_year,
            this_sales_data.ungraded_sale,
            this_sales_data.grade_4_sale,
            this_sales_data.grade_6_sale,
            this_sales_data.grade_8_sale,
            this_sales_data.grade_9_plus_sale,
        ]
    )

delete_file_if_exists(OUTPUT_FILE_PATH)
write_csv_file(OUTPUT_FILE_PATH, comics)
