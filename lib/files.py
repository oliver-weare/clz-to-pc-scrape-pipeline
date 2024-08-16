import csv, os


def delete_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def get_csv_data(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        data = [row for row in csv_reader]

        return data


def write_csv_file(file_path, data):
    with open(file_path, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        for row in data:
            csv_writer.writerow(row)
