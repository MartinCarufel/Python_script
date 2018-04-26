#coding:utf-8

import csv


file = open('DS4 connection.csv')
csv_line = csv.reader(file)

output_file = open('DS4-Analog Harness.xml','w')


x_line = []

output_file.write("<Map>\n")
output_file.write("\t<Devices>\n")

output_file.write("\t\t<Device model=\"8223\" deviceNo=\"1\">\n")


for row in csv_line:
    if row[6] == "SeaDAC ISO 8223":
        output_file.write("\t\t\t<Port name=\"{}\", type=\"{}\", portNo=\"{}\", comment=\"{}-{} {}\", negateValue=\"{}\"/>\n" .format(row[10],row[7], row[9],row[0],row[4],row[3],row[5],row[8]))

output_file.write("\t\t</Devices>\n")


file.close()
output_file.write("\t\t<Device model=\"8224\" deviceNo=\"2\">\n")
file = open('DS4 connection.csv')
csv_line = csv.reader(file)

for row in csv_line:
    if row[6] == "SeaDAC ISO 8224":
        output_file.write("\t\t\t<Port name=\"{}\", type=\"{}\", portNo=\"{}\", comment=\"{}-{} {}\", negateValue=\"{}\"/>\n" .format(row[10],row[7], row[9],row[0],row[4],row[3],row[5],row[8]))

output_file.write("\t\t</Devices>\n")

output_file.write("\t</Devices>\n")
output_file.write("\t<Groups />\n")
output_file.write("\t<BoolAnalogs/>\n")
output_file.write("</Map>")

file.close()
output_file.close()