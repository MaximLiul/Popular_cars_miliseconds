import pandas as pd
import time
import datetime

cars_data = pd.read_csv('Car_Data_In_Seconds.csv', encoding = 'unicode_escape')

#print(type(carsData['Date'][0]))

def date_to_seconds(path_to_data_frame, time_column_name, new_data_frame_name):
    data_frame = pd.read_csv(path_to_data_frame, encoding = 'unicode_escape')
    data_frame['Normalized Date'] = 0
    minimum_date_str = data_frame[time_column_name].min()
    minimum_date_date = datetime.datetime.strptime(minimum_date_str, '%Y-%m-%d')
    for index in range(len(data_frame.index)):
        duration_in_seconds = datetime.datetime.strptime(data_frame[time_column_name][index], '%Y-%m-%d') - minimum_date_date
        data_frame['Normalized Date'][index] = duration_in_seconds.total_seconds()

    return data_frame.to_csv(new_data_frame_name, index=False)

#date_to_seconds('Car_Data_Changed.csv', 'Date', 'Car_Data_In_Seconds.csv')

def filter_by_days(path_to_data_frame, date_time_column_name, time_in_seconds_column_name, filtering_date_str, new_data_frame_name):
    data_frame = pd.read_csv(path_to_data_frame, encoding='unicode_escape')
    minimum_date_str = data_frame[date_time_column_name].min()
    minimum_date = datetime.datetime.strptime(minimum_date_str, '%Y-%m-%d')
    filtering_day = datetime.datetime.strptime(filtering_date_str, '%Y-%m-%d')
    filtering_time = filtering_day - minimum_date
    filtering_time_in_seconds = filtering_time.total_seconds()
    #print(data_frame[time_in_seconds_column_name][10] > filtering_time_in_seconds)
    data_frame_filtered = data_frame.loc[data_frame[time_in_seconds_column_name] > filtering_time_in_seconds]
    #print(data_frame_filtered)
    return data_frame_filtered.to_csv(new_data_frame_name, index=False)

#filter_by_days('Car_Data_In_Seconds.csv', 'Date', 'Normalized Date', '2019-12-12', 'Filtered_By_Days.csv')
#filter_by_days_df.to_csv('filter_by_days.csv', encoding='unicode_escape')
#df_filtered = pd.read_csv('Filtered_By_Days.csv', encoding = 'unicode_escape')

#print(df_filtered['Price'])




def filter_by_total_income(path_to_data_frame, price_column_name, brand_column_name, filtering_income_value, new_data_frame_name):
    data_frame = pd.read_csv(path_to_data_frame, encoding='unicode_escape')
    #print(data_frame.groupby(brand_column_name)[price_column_name].sum())
    total_income_of_brands_df = data_frame.groupby(brand_column_name) [price_column_name].sum()
    #print(total_income_of_brands_df > filtering_income_value)
    df_filtered_by_income = total_income_of_brands_df[total_income_of_brands_df > filtering_income_value]
    return df_filtered_by_income
    #return df_filtered_by_income.to_csv(new_data_frame_name


#filter_by_total_income('Filtered_By_Days.csv', 'Price', 'Brand', 10000000, 'Filtered_By_Income.csv')

df_filtered_by_total_income = filter_by_total_income('Filtered_By_Days.csv', 'Price', 'Brand', 10000000, 'Filtered_By_Income.csv')

print(len(df_filtered_by_total_income.index))







#date_to_days('Car_Data_Changed.csv', 'Date', 'Car_Data_In_Days.csv')
#print(type(int(cars_data['Normalized Date'][4])))
#print(datetime.datetime.strptime(cars_data['Date'].max(), '%Y-%m-%d').date())
#print(cars_data['Brand'].unique())
#datetime.datetime.strptime(carsData['Date'].max()), '%Y-%m-%d %H:%M:%S.%f')
#print(cars_data['Normalized Date'][9])
