import pandas as pd
import json
df = pd.read_csv('movie_test_file.csv')
# any operations on dataframe df
df.to_json('movie_test_file2.json')
with open('movie_test_file2.json', 'r') as handle:
    parsed = json.load(handle)
