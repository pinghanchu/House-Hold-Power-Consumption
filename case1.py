#!/usr/bin/python
import datetime
import time
import csv
import sqlite3
conn = sqlite3.connect('household.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS House''')

cur.execute('''
CREATE TABLE House (Date TEXT, Time TEXT, Year INTEGER,Month INTEGER, Day INTEGER, Hour INTEGER, Min INTEGER, Sec INTEGER, Global_active_power FLOAT, Global_reactive_power FLOAT, Voltage FLOAT, Global_intensity FLOAT, Sub_metering_1 FLOAT, Sub_metering_2 FLOAT, Sub_metering_3 FLOAT)''')


with open('household_power_consumption.txt','rb') as csvfile:
    sreader = csv.reader(csvfile,delimiter = ';')
    next(sreader)
    for row in sreader:
        y0 = row[0]
        y1 = row[1]
        y2 = row[2]
        y3 = row[3]
        y4 = row[4]
        y5 = row[5]
        y6 = row[6]
        y7 = row[7]
        y8 = row[8]
        x0 = row[0].split("/")
        z1 = x0[0]
        z2 = x0[1]
        z3 = x0[2]
        x1 = row[1].split(":")
        z4 = x1[0]
        z5 = x1[1]
        z6 = x1[2]
        print y0, y1, z3, z2, z1, z4,z5,z6,y2, y3,y4,y5,y6,y7,y8
        cur.execute('INSERT INTO House (Date,Time,Year,Month,Day,Hour,Min,Sec,Global_active_power,Global_reactive_power,Voltage,Global_intensity,Sub_metering_1,Sub_metering_2,Sub_metering_3) VALUES (?,?,?,?,?,?,?, ?, ?, ?,?,?,?,?,?)', ( y0,y1,z3,z2,z1,z4,z5,z6,y2,y3,y4,y5,y6,y7,y8) )
conn.commit()

