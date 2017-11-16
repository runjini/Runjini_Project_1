import pandas as pd
df = pd.read_csv('Public_Art.csv')
# any operations on dataframe df
df.to_json('Public_Art.json')
print ("Conversion complete!")
