from data_cleaning import change_to_nan, remove_missing_data
from user_communication import FileToDataFrame

file1 = FileToDataFrame()
file1.view_directory()
data = file1.read_file(input('\nGive ID of file You want to analyze: \n'))
print(data)