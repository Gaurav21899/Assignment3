import arcpy
import os

# Setting the Work Space for Feature Class and Fields
arcpy.env.workspace = r"D:\Sem-3\Programming for GIS-3\Assignment3\ProProject_AutomatingUsingLists\ProProject_AutomatingUsingLists.gdb"

# Opening text file
folder_path = r"D:\Sem-3\Programming for GIS-3\Assignment3"
output_text_file = "MajorAttraction.txt"
output_file_path = os.path.join(folder_path, output_text_file)
print(output_file_path)
file_obj = open(output_file_path, "w")

# Creating list of field from Feature Class
field_obj = arcpy.ListFields("MajorAttractions")
print("MajorAttraction feature Class and Field Descriptions")
file_obj.write("MajorAttraction feature Class and Field Descriptions \n")

# Loop through list of field
for field in field_obj:
    print("Name: {}, Type: {}, size: {}".format(field.name, field.type, field.length))
    file_obj.write("Name: {}, Type: {}, size: {} \n".format(field.name, field.type, field.length))

    print(".................................................")
    file_obj.write("........................................ \n")

# Closing the Text File
file_obj.close()
print("Process Completed")

