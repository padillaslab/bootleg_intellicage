from datetime import datetime
import serial
import json
import serial.tools.list_ports
import csv
import sys

ard = serial.Serial(sys.argv[1], 9600)

rec_start_time = datetime.now()
csv_name = 'HE_output' ##csv name
csv_name += '_' + str(rec_start_time.year) + '_' + str(rec_start_time.month) + '_' + str(rec_start_time.day) + '_' + str(rec_start_time.hour) + '_' + str(rec_start_time.minute) ##dating csv file
csv_name += '.csv'

with open(csv_name, 'w') as HE_output:
        HE_writer = csv.writer(HE_output)
        HE_writer.writerow(["ID", "Timestamp", "Count 1", "Count 2", "Count 3", "Count 4", "Count 5", "Count 6", "Count 7", "Count 8", "Count 9", "Count 10"])
        while 1:
            json_output = json.loads(ard.readline().strip())

            data_arr = [json_output["ID"], datetime.now(), json_output["count"]]
            HE_writer.writerow(data_arr) 