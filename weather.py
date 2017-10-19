from bs4 import BeautifulSoup
import urllib
import datetime

now = datetime.datetime.now()
weatherURL = "http://www.wunderground.com/history/airport/KNYC/"+str(now.year)+"/"+str(now.month)+"/"+str(now.day)+"/MonthlyHistory.html"
r = urllib.urlopen(weatherURL).read()
soup = BeautifulSoup(r,'html.parser')
calendar = soup.find('table', {'id':'obsTable'})
count =0
mydata = calendar.findAll('tbody')
print("---------------------------------------------------------")
print("\tDays of the month that have passed")
print("---------------------------------------------------------")
print('  Day of month \t\tHigh\tAvg\tLow')
for data in mydata:
	count = count +1
	if(count !=1):
		print '\t'+str(data.find('td').find('a').text) + '\t\t'+str(data.findAll('td')[1].text).strip() + '\t'+str(data.findAll('td')[2].text).strip() +'\t'+ str(data.findAll('td')[3].text).strip() 
	
futureWeatherURL= "http://www.wunderground.com/history/airport/KNYC/"+str(now.year)+"/"+str(now.month)+"/"+str(now.day)+"/MonthlyCalendar.html?req_city=Central%20Park&req_state=NY&reqdb.zip=10106&reqdb.magic=2&reqdb.wmo=99999#calendar"
r = urllib.urlopen(futureWeatherURL).read()
soup = BeautifulSoup(r,'html.parser')
calendar = soup.findAll(class_=['day forecast','day future'])
print("\n\n---------------------------------------------------------")
print("\tDays of the month that have not passed yet")
print("---------------------------------------------------------")
print('   Future Day\t\tMaximum\t\tMinimum')
for futureDay in calendar:
	print  '\t'+str(futureDay.find('a').text).strip() +'\t\t'+(futureDay.find('span',{'class':'high'}).text).strip() +'\t\t'+(futureDay.find('span',{'class':'low'}).text).strip()