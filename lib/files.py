import pandas

from paths import INPUT_FILE_PATH


def get_csv_data():
    csv_data = pandas.read_csv(INPUT_FILE_PATH)
    return csv_data
