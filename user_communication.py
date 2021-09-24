import pandas as pd
import numpy as np
import os
from tabulate import tabulate

class FileToDataFrame:
    def __init__(self):
        self.file_id = -1
        self.files = []
        self.chosen_file_name = ''

    def read_file(self, id):
        self.file_id = int(id)
        # user gives id as shown in view_directory (indexing from 1), so it has to decremented
        self.chosen_file_name = self.files[self.file_id - 1]
        if self.chosen_file_name.endswith('.csv'):
            data = pd.read_csv(f'csv_files/{self.chosen_file_name}')
        elif self.chosen_file_name.endswith('.xlsx'):
            data = pd.read_excel(f'csv_files/{self.chosen_file_name}')
        return data

    def view_directory(self):
        self.files = os.listdir('csv_files')
        table = []
        for file_id in range(len(self.files)):
            #file_id is incremented to display files starting with index 1 not 0
            table.append([file_id+1, self.files[file_id]])
        print(tabulate(table, headers=['file ID', 'file name'], tablefmt='orgtbl'))



