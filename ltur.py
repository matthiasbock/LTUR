#!/usr/bin/python

from httpclient import HttpClient

c = HttpClient(debug=True)

c.GET("http://www.ltur.com/de/bahn.html?omnin=DB-DE")

q = "/index/search/?mnd=de&lang=de_DE&searchin=DE-SB-VI&trip_mode=trip_simple"
q += "&from_spar=Berlin+Gesundbrunnen"
q += "&to_spar=M%C3%BCnchen+Hbf"
q += "&start_datum=14.05.2013"
q += "&start_time=18%3A40"
q += "&end_datum=15.05.2013"
q += "&end_time=18%3A40"
q += "&SEA_adults=1&SEA_kids1=0&SEA_kids2=0&SEA_adult1=&SEA_adult2=&SEA_adult3=&SEA_adult4=&SEA_adult5=&SEA_kid11=&SEA_kid12=&SEA_kid13=&SEA_kid14=&SEA_kid15=&trainclass_spar=2&x=41&y=15"
c.GET(q)

open('ltur.html','w').write(str(c.Page))
