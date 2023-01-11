import pandas as pd

df = pd.DataFrame()

print(type(df))
# <class 'pandas.core.frame.DataFrame'>

df = pd.read_csv('PandasExample.csv')
print(df)

# header = ['name'               'area'  'country_code2'          'country_code3']
# data = ['Afghanistan'          652090  'AF'                               'AFG']

print(df.head())
#  header = ['name'               'area'  'country_code2'          'country_code3']
# data = ['Afghanistan'          652090  'AF'                               'AFG']

print(df.tail())
# header = ['name'               'area'  'country_code2'          'country_code3']
# data = ['Afghanistan'          652090  'AF'                               'AFG']

print(df.head(1))  # print first row
# header = ['name'  'area'  'country_code2'   'country_code3']

print(df.tail(1))  # print last row
# writer.writerow(data) NaN NaN          NaN

print(df.iloc[0])
# import csv       'country_code3']
# Name: (header = ['name',  'area',  'country_code2'), dtype: object

print(df.iloc[2])
# import csv      NaN
# Name: (with open('PandasExample.csv',  'w',  encoding='UTF8') as f:), dtype: object

print(df.values)
# [[" 'country_code3']"]
#  [" 'AFG']"]
#  [nan]
#  [nan]
#  [nan]
#  [nan]
#  [nan]
#  [nan]]

df = pd.read_csv('PandasExample.csv', chunksize=2)

for chunk in df:
    print(chunk)
    # header = ['name'       'area'  'country_code2'   'country_code3']
    # data = ['Afghanistan'  652090  'AF'                        'AFG']
    #                                                             import csv
    # with open('PandasExample.csv'  'w'  encoding='UTF8') as f:           NaN
    #     writer = csv.writer(f)    NaN  NaN                               NaN
    #                                      import csv
    #     # write the header      NaN NaN           NaN
    #     writer.writerow(header) NaN NaN           NaN
    #                                    import csv
    #     # write the data      NaN NaN           NaN
    #     writer.writerow(data) NaN NaN           NaN

df = pd.read_csv('PandasExample.csv')

df = df[df['area'] > 650000]

print(df)
#                     name      area country_code2 country_code3
# 0  data = ['Afghanistan'  652090.0          'AF'        'AFG']
# 2           data = ['IN'  752090.0            IN          'IN'
