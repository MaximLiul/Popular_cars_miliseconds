import pandas as pd
import time
import datetime
import random
#carsData = pd.read_csv('Car_Data_With_Date.csv', encoding = 'unicode_escape')


def random_date(start_date, end_date, format):
    start_time = time.mktime(time.strptime(start_date, format))
    end_time = time.mktime(time.strptime(end_date, format))
    random_time = start_time + random.random() * (end_time - start_time)
    return time.strftime(format, time.localtime(random_time))

print(random_date("1/1/2019", datetime.date.today().strftime('%d/%m/%Y'), '%d/%m/%Y'))
'''
def cars_data_filtered_by_time(number_of_days_ago):
    today = datetime.date.today()
    delta = datetime.timedelta(days=number_of_days_ago)
    comparing_day = today - delta
    datetime.datetime.strftime(comparing_day, '%d/%m/%Y')

    print(type(comparing_day))
    car_selling_day = datetime.datetime.fromtimestamp(time.mktime(time.strptime(carsData['Date'][2], '%d/%m/%Y')))
    print(car_selling_day, "day")
    #print(car_selling_day > comparing_day)
    #cars_data_filterred_by_time = carsData.loc[time.strptime(carsData['Date'], '%d/%m/%Y') > comparing_day]
    #return cars_data_filterred_by_time
    return today

print(cars_data_filtered_by_time(30))
'''