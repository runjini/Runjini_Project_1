csvfile = open('movie_test_file.csv', 'r')
jsonfile = open('movie_test_file.csv'.replace('.csv', '.json'), 'w')

jsonfile.write('{"' + 'movie_test_file.csv'.replace('.csv', '') + '": [\n') # Write JSON parent of data list
fieldnames = csvfile.readline().replace('\n','').split(',')        # Get fieldnames from first line of csv
num_lines = sum(1 for line in open('movie_test_file.csv')) - 1              # Count total lines in csv minus header row

reader = csv.DictReader(csvfile, fieldnames)
i = 0
for row in reader:
  i += 1
  json.dump(row, jsonfile)
  if i < num_lines:
    jsonfile.write(',')
  jsonfile.write('\n')
jsonfile.write(']}')
