#!/usr/bin

import os, time, datetime, sqlite3


conn = sqlite3.connect('/home/time_for_pi/frontpage/timeserver.db', timeout=1)
curs=conn.cursor()
gps_select="SELECT* FROM gps_check"
curs.execute(gps_select)
gps = [dict(gpstime=row[1], gpsstatus=row[2], longitude=row[3], lattitude=row[4]) for row in curs.fetchall()]
print type(gps)
now = datetime.datetime.now()
os.system("echo 'This is the noon gun firing timer. \n The time is now {0} \n GPS DATA: \n {1}' | mail -s 'Time' -t timeservice@list.saao.ac.za".format(str(now), str(gps[0])))
