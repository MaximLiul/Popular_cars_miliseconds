import pandas as pd
import time
import datetime
import random
data_frame = pd.read_csv('Car_Data.csv', encoding = 'unicode_escape')
data_frame['Date'] = 0

def random_date():
    today = datetime.date.today()
    delta = datetime.timedelta(days=500*random.random())
    random_day = today - delta
    return random_day
#print(cars_data_filtered_by_time())

for index in range(len(data_frame.index)):
    data_frame.iloc[index, 9] = random_date()

data_frame.to_csv('Car_Data_Changed.csv', index=False)

