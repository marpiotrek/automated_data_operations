import pandas as pd
import numpy as np


def read_file(filename):
    data = pd.read_csv(f'csv_files/{filename}')
    return data


def remove_missing_data(data):
    pass


def change_to_nan(data, nan_alikes=[]):
    '''
    replaces NaN - alike words to only NaN. By default it detects cells like
    'Null', 'NA', 'N/A', 'not applicable', 'not available', 'no answer' and changes them to NaN
    :param data: data frame
    :param nan_alikes: list of values to be considered as NaNs
    :return: data frame
    '''
    #using .str.contains("Null|NA|not applicable") could also work for specified column but
    #it returns error when there are already cells with NaN
    NaN_like_data = ['null', 'na', 'n/a', 'not applicable', 'not available', 'no answer'] + nan_alikes
    for word in NaN_like_data:
        data[data.apply(lambda x: x.astype(str).str.lower()) == word] = np.nan
    return data


def remove_duplicates(data):
    pass