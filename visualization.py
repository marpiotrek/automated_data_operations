import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def extract_columns(data):
    '''
    tutaj zrobić
    x, y, z = data.T
    tylko w zależności od wymiaru array
    :param array:
    :return:
    '''
    columns = data.columns
    for column in columns:
        print(data[f'{column}'])
