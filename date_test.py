import pandas as pd
import datetime
cars_data = pd.read_csv('Car_Data_Changed.csv', encoding = 'unicode_escape')

#print(type(cars_data['Date']), 'column')
#print(type(cars_data['Date'][0]), 'cell')
cars_date1 = datetime.datetime.strptime(cars_data['Date'][0], '%Y-%m-%d')
cars_date2 = datetime.datetime.strptime(cars_data['Date'][15], '%Y-%m-%d')
'''
print(cars_date1, 'cars_date1')
print(cars_date2, 'cars_date2')
print(cars_date1 - cars_date2)
'''
print(cars_data.dtypes)