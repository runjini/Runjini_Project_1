import pandas as pd
df = pd.read_csv('Hawaii_Farmer_s_Markets.csv')
# any operations on dataframe df
df.to_json('Hawaii_Farmer_s_Markets.json')
print ("Conversion complete!")
