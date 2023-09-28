import arcpy

# Setting Workspace
arcpy.env.workspace = r"D:\Sem-3\Programming for GIS-3\Assignment3\ProProject_AutomatingUsingLists\ProProject_AutomatingUsingLists.gdb"
fc_list = arcpy.ListFeatureClasses()


buffer_distance = 0
for fc in fc_list:
    fc_obj = arcpy.Describe(fc)
    shape_type = fc_obj.shapeType

# Assigning buffer distance based on a feature class shape type
# point: 200 feet, polyline: 400 feet, polygon: 600 feet

    if shape_type == "Point":
       buffer_distance = "200 feet"
    elif shape_type == "Polyline":
       buffer_distance = "400 feet"
    elif shape_type == "Polygon":
       buffer_distance = "600 feet"

    output_buffer = fc + "_Buffer"

# Calculating buffer for each feature class
    arcpy.analysis.Buffer(fc, output_buffer, buffer_distance)

print("Process Completed")

