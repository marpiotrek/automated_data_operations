from data_cleaning import change_to_nan, remove_missing_data
from user_communication import FileToDataFrame
from information import DataInformation


file1 = FileToDataFrame()
#view files in csv_files
file1.view_directory()
#choose ID corresponding to particular file, and save it as a data frame
data = file1.read_file(input('\nGive ID of file You want to analyze: \n'))
print(f'This is your data:\n {data}\n')
stats1 = DataInformation(data)
stats1.missing_values()