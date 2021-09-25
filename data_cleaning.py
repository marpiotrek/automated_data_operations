import pandas as pd
import numpy as np


def remove_missing_data(data):
    pass


def change_to_nan(data, nan_alikes=[]):
    '''
    replaces NaN - alike words to only NaN. By default it detects cells like
    'null', 'nan', 'n/a', 'none' , 'not applicable', 'not available', 'no answer' and changes them to NaN
    :param data: data frame
    :param nan_alikes: list of values to be considered as NaNs
    :return: data frame
    '''
    #all characters in compared strings need to be lowercase letters

    nan_alikes = list(map(lambda x: x.lower(), nan_alikes))
    NaN_like_data = ['null', 'nan', 'n/a', 'na', 'none', 'not applicable', 'not available', 'no answer'] + nan_alikes
    for word in NaN_like_data:
        print(word)
        data[data.apply(lambda x: x.astype(str).str.lower()) == word] = np.nan
    return data


def remove_duplicates(data):
    pass