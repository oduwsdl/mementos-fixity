#!/usr/bin/python

import sys
import json
import requests
import datetime

def getmementosFromTimeTravel(url):
	pages = []
	plist = []
	url = url.strip()
	try:
		if(len(url)>0):
			firstChoiceAggregator = "http://timetravel.mementoweb.org/timemap/json/"
			timemapPrefix = firstChoiceAggregator + url

			r = requests.get(timemapPrefix, timeout=100, allow_redirects=True,
                             headers={"Accept" : "application/json" })
			payload = r.json()

			if len(payload) > 0:
				if 'timemap_index' in payload:
					for timemap in payload['timemap_index']:
						timemapLink = timemap['uri'].replace('/timemap/json/', '/timemap/link/')
						r = requests.get(timemapLink, timeout=100, allow_redirects=True)
						v2 = r.content.split('\n');
						for v3 in v2:
							nnew = v3.split(' GMT",')
							for v4 in nnew:
								v5 = ", "+v4 + ' GMT"'
								if ("datetime=" in v5) and (('rel="memento"' in v5) or ('rel="first last memento"' in v5) or ('rel="last memento"' in v5)  or ('rel="first memento"' in v5)):
									plist.append(v5)
				elif 'mementos' in payload:
					timemapLink = payload['timemap_uri']['json_format'].replace('/timemap/json/', '/timemap/link/')
					r = requests.get(timemapLink, timeout=100, allow_redirects=True)
					v2 = r.content.split('\n');
					for v3 in v2:
						nnew = v3.split(' GMT",')
						for v4 in nnew:
							v5 = ", "+v4 + ' GMT"'
							if ("datetime=" in v5) and (('rel="memento"' in v5) or ('rel="first last memento"' in v5) or ('rel="last memento"' in v5)  or ('rel="first memento"' in v5)):
								plist.append(v5)
		return plist
	except Exception as e:
		print 'ERROR '
		print (e)


m = getmementosFromTimeTravel(sys.argv[1]);

if m != None:
	for mm in m:
		urim = mm.split('<',1)[1].split('>',1)[0]
		date_time = mm.split('; datetime="',1)[1].split('"',1)[0]
		timestamp = datetime.datetime.strptime(date_time, '%a, %d %b %Y %H:%M:%S GMT').strftime('%Y%m%d%H%M%S')
		print timestamp+" "+urim

