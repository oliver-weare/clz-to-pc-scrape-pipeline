import csv

from paths import INPUT_FILE_PATH


def get_csv_data():
    with open(INPUT_FILE_PATH) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        data = [row for row in csv_reader]

        return data
