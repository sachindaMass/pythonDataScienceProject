import pandas as pd

df = pd.read_csv('HousePrices.csv', parse_dates=True)

print(df)
#                     date      price  bedrooms  ...       city   statezip  country
# 0  2014-05-02 00:00:00.0   313000.0       3.0  ...  Shoreline   wa 98133      USA
# 1  2014-05-02 00:00:00.0  2384000.0       5.0  ...    Seattle   wa 98119      USA
# 2  2014-05-02 00:00:00.0   342200.0       3.0  ...    Seattle   wa 98042      USA
# 3  2014-05-02 00:00:00.0   420000.0       3.0  ...       Kent  wa 980008      USA
