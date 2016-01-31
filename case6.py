#!/usr/bin/python
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
import sqlite3
conn = sqlite3.connect('household.sqlite')
cur = conn.cursor()


month_list=list()
time_list=list()
power_list=list()
cur.execute('SELECT Year, Month FROM House ')
for row in cur:
    time_list = (row[0],row[1])
    month_list.append(time_list)

year_list=list()
temp1 = 0
temp2 = 0
for ii in month_list:
    if ii[0] != temp1 or ii[1] != temp2:
        year_list.append(ii)
    temp1 = ii[0]
    temp2 = ii[1]
for iii in year_list:
#    print iii[0],iii[1]
    cur.execute('SELECT Sub_metering_3 FROM House WHERE Year =? AND Month =? ',(iii[0],iii[1]))
    sum = 0
    for row in cur:
        #print row[0],sum
        if isinstance(row[0],float):
            sum = sum + row[0]
    power_list.append(sum)
dates = list()
for iv in year_list:
    xx = str(iv[1])+"/"+str(iv[0])
    dates.append(xx)
x = [dt.datetime.strptime(d,'%m/%Y').date() for d in dates]

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=182))
plt.plot(x,power_list)
plt.title('Sub Metering 3 (heater/air-conitioner) per Month (watt hour)')
plt.gcf().autofmt_xdate()
plt.show()
plt.savefig('case6.png')
