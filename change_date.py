import pandas as pd
import random
import time
import datetime
from datetime import date


def change_date(start_date, end_date, format, name_of_the_file_to_change, name_of_a_changed_file):
    file_to_change = pd.read_csv(name_of_the_file_to_change, encoding = 'unicode_escape')
    file_to_change['Date'] = 0

    def random_date(start_date, end_date, format):
        start_time = time.mktime(time.strptime(start_date, format))
        end_time = time.mktime(time.strptime(end_date, format))
        random_time = start_time + random.random()*(end_time - start_time)
        date = datetime.datetime.fromtimestamp(random_time/1000.0)
        print(date)
        #return time.strftime(format, time.localtime(random_time))

    for index in range(len(file_to_change.index)):
        file_to_change.iloc[index, 9] = random_date(start_date, end_date, format)

    return file_to_change.to_csv(name_of_a_changed_file, index=False)

change_date("1/1/2019", date.today().strftime('%d/%m/%Y'), '%d/%m/%Y', 'Car_Data.csv', 'Car_Data_With_Date.csv')
#data_frame = pd.read_csv('Car_Data_With_Date.csv')
#print(type(time.strptime(data_frame.iloc[0,9], '%d/%m/%Y')))
#print(time.strptime(data_frame.iloc[0,9], '%d/%m/%Y') > time.strptime('21/04/2995', '%d/%m/%Y') )
#print(data_frame.iloc[0,9])


