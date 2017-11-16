import csv
import json
with open('movie_test_file.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    data_list = list()
    for row in reader:
        data_list.append(row)
data = [dict(zip(data_list[0],row)) for row in data_list]
data.pop(0)
s = json.dumps(data)
print (s)
