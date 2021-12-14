import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('players.csv')
print(df)

profile = ProfileReport(df)
profile.to_file(output_file="Analysed_data.html")
