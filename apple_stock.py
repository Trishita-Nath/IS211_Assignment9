from bs4 import BeautifulSoup
import urllib

r = urllib.urlopen('http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices').read()
soup = BeautifulSoup(r,'html.parser')
data = soup.find('tbody')
stockData = data.findAll('tr')
previousDay =''
print '-------------------------------'
print '   Date \t Price'
print '-------------------------------'
for dailyData in stockData:
	count = dailyData.findAll('span')
	if(previousDay != dailyData.findAll('span')[0].contents[0]):
		previousDay = dailyData.findAll('span')[0].contents[0]
		print dailyData.findAll('span')[0].contents[0] + '\t' + dailyData.findAll('span')[3].contents[0]
