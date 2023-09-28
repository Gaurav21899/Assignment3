import os

folder_path = r"D:\Sem-3\Programming for GIS-3\Assignment3"
file_name = "When a friend calls to me.txt"

file_path = os.path.join(folder_path, file_name)
file_obj = open(file_path, 'r')

lines = file_obj.readlines()
for line in lines:
    print(line)

