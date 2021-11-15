import csv


class OpenFile(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


def csv_reader(file_name):
    w_list = []

    with OpenFile(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            for key in row:
                row[key] = float(row[key]) * 2
            w_list.append(row)

    return w_list


def csv_writer(file_name, arg_list):
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = arg_list[0].keys()

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for element in arg_list:
            writer.writerow(element)


if __name__ == '__main__':
    weather_list = csv_reader('weather.csv')

    csv_writer('weather_modified.csv', weather_list)
