import sys, os, tkFileDialog, tkMessageBox
import csv
import json
# from Tkinter import *
# from pandas.io.json import json_normalize
from operator import itemgetter

with open('data1.json') as in_f:
    data = json.loads(in_f.read())

with open("RequiredDataSet.csv", "wb+") as csv_file:
    csv_writer = csv.writer(csv_file)
    for item in data:
    	for i in range(len(item['stays'])):
    		for j in range(len(item['stays'][i]['room_details'])):
    			#csv_writer.writerow([ item['booking_date'], item['stays'][i]['property_id'],item['stays'][i]['room_details'][j]['id'],item['stays'][i]['check_in'],item['stays'][i]['check_out'],item['stays'][i]['room_details'][j]['pricing_detail']['room_rate']] )
    			csv_writer.writerow([ item['booking_date'],item['channel'], item['stays'][i]['property_id'],item['stays'][i]['room_details'][j]['name'],item['stays'][i]['room_details'][j]['id'],item['stays'][i]['check_in'],item['stays'][i]['check_out'],item['stays'][i]['room_details'][j]['pricing_detail']['room_rate'],item['stays'][i]['room_details'][j]['booking_status']] )
    			
            #csv_writer.writerow([item['stays'][0]['check_in'],item['stays'][0]['check_out'] ])



            #csv_writer.writerow([item['stays'][0]['check_in'],item['stays'][0]['check_out'] ])


