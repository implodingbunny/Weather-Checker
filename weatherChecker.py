#!/usr/bin/python

import urllib
import time

# # # To-Do:
# # # - Alarm dependent on time and day
# # # - 

weatherToday = ""
time = ""
timevalid = True
today = ""
daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weatherConditions = ["Rain", "Sun", "Cloud"]

location = raw_input("Enter your postcode: ")
location = location.lower()

def UpdateWeather(location, weathertoday, Today):
	running = True
	while running = True:
		#read weather at location from external source
		sock = urllib.urlopen("http://www.bbc.co.uk/weather/" + location)
		raw_html = sock.readlines()
		sock.close()

		#HTML copied, need to extract weather from line 621 ?and temp from line 624?
		# # change from static location to dynamic
		for weather in weatherConditions:
			if weather in raw_html[621]:
				weatherToday = weather
		
		#Weekday on line 618
		for day in daysOfWeek:
			if day in raw_html[617]:
				today = day

		print Today
		print weathertoday

		time.sleep(43200)

UpdateWeather(location, weathertoday, Today)