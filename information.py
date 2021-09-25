import pandas as pd
import numpy as np

class DataInformation:
    def __init__(self, data):
        self.data = data
        self.num_of_rows = self.data.shape[0]
        self.num_of_columns = self.data.shape[1]

    def missing_values(self):
        '''
        prints information about missing values in analyzed dataset
        :return:
        '''
        #stores information about number of NaN values in each column as a list
        nans_per_column = self.data.isnull().sum().tolist()
        #first column of data frame about NaNs containing columns names
        col_names = pd.Series(self.data.columns, name="column name")
        #second column: total rows in analyzed data frame
        col_rows_in_col = pd.Series([self.num_of_rows]*self.num_of_columns, name="total rows")
        #third column: sum of NaNs in each column
        col_nans_in_col = pd.Series(nans_per_column, name="total NaN")
        #fourth column: percentage of NaNs in each column
        col_percent_of_nans = pd.Series([x/self.num_of_rows*100 for x in nans_per_column], name="NaNs percentage [%]")
        #all above series joined together into data frame
        nan_stats_table = pd.concat([col_names, col_rows_in_col, col_nans_in_col, col_percent_of_nans], axis=1)
        sum_of_nans = sum(nans_per_column)
        #perecentage of NaNs in whole data frame
        percent_of_nans_total = sum_of_nans/self.num_of_rows/self.num_of_columns*100
        #find columns with missing values percentage bigger than 30%
        col_with_to_many_nan = col_names[col_percent_of_nans>30]
        #convert it to single string seperated by coma
        str_col_with_to_many_nan = ', '.join(col_with_to_many_nan)
        #print information about missing values
        print(f'\nNumber of missing values in data: {sum_of_nans}')
        print(f'Percentage of missing values in the whole data: {round(percent_of_nans_total, 2)}%')
        print('Table with informations about missing values for each column:\n')
        print(nan_stats_table)
        if len(col_with_to_many_nan) > 1:
            print(f'\nThere are {len(col_with_to_many_nan)} columns with more than 30% missing values. \n'
                  f'Those columns are: {str_col_with_to_many_nan}.')
        elif len(col_with_to_many_nan) == 1:
            print(f'\nThere is {len(col_with_to_many_nan)} column with more than 30% missing values. \n'
                  f'This column is: {str_col_with_to_many_nan}.')

