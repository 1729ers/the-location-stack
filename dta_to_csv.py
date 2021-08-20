import pandas as pd
data = pd.io.stata.read_stata('/content/WRLURI_01_15_2020.dta')
data.to_csv('WRLURI_01_15_2020.csv',index=False)