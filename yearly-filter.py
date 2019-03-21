#!/usr/bin/python

import sys

final_selected_set = {}

for line in sys.stdin:
	tokenss = line.split()
	urim =  tokenss[1]
	timestamp = tokenss[0]
	year = timestamp[0:4]
	archive_name = urim.split("://",1)[1].split("/",1)[0]
	#print urim, timestamp, year, archive_name
	if archive_name not in final_selected_set:
		final_selected_set[archive_name] = {}
	if year not in final_selected_set[archive_name]:
		final_selected_set[archive_name][year] = timestamp+' '+urim

for archive,v in final_selected_set.items():
	for y in range(1996,2019):
		if str(y) in v:
			print v[str(y)]
