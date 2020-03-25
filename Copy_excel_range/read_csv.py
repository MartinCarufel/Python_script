import csv

file_name = "File_list.csv"
path_source = "C:/Drive-W/test_veh_profile/sense/Excel/from_old_temp/"
path_target = "C:/Drive-W/test_veh_profile/sense/Excel/"


with open(file_name, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        for item in range(len(line)):

            f = open(path_source + line[0], 'r')
            print(line[item])
            f.close()


