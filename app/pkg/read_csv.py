import csv
import json

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []

        for row in reader:
            iterable = zip(header, row)
            country_dic = {key: value for key, value in iterable}
            data.append(country_dic)
        return data

if __name__ == '__main__':
    data = read_csv('d:/CFMe/file/data.csv')
    data_json = json.dumps(data, ensure_ascii=False, indent=4)
    print(data_json)