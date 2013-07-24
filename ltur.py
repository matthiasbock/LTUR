#!/usr/bin/python

from httpclient import HttpClient
from htmlparser import between

#
# Search form:
# http://www.ltur.com/de/bahn.html?omnin=TopNavi-DB
#

def testGET():
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

class Row:
	def __init__(self, row):
		date = between(row, '<td class="', '</td>', skip=1)
		time = between(row, '<td class="', '</td>', skip=2)
		self.departure = between(date, '>', '<')+' '+between(time, ' ', '<', skip=1)
		self.arrival = between(date, '>', '-', skip=1)+' '+between(time, ' ', '-', skip=2)
		self.price = between(row, '<label>', '</label>').split(' ')[0]
	
	def __str__(self):
		return self.price+' EUR: '+self.departure+' - '+self.arrival

def parse(resultsPage):
	results = between(resultsPage, '<table id="connectionList"', '</table>')
	skip = 0
	row = ' '
	while row != '':
		row = between(results, '<tr>', '</tr>', skip=skip)
		if row != '':
			if 'special-offer' in row:
				print Row(row)
		skip += 1

parse( open('details.html').read() )