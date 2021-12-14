# PandasProfiling

## Install Python and Run Locally

Install Pandas Library

```bash
pip instasll pandas
```

pip install pandas profiling


```

## Running the python code ##

import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('players.csv')
print(df)

profile = ProfileReport(df)
profile.to_file(output_file="Analysed_data.html")
```

## Jupyter Notebook
```bash
pip install jupyter
```

## Start the Notebook server

```bash
python -m Notebook
```

