from bs4 import BeautifulSoup
import urllib

r = urllib.urlopen('http://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns').read()
soup = BeautifulSoup(r,'html.parser')
row = soup.find(class_='data')
row2 = row.find_all(class_=['row1','row2'])
count =0

for data in row2:
	count=count +1
	if(count == 1):
		print "----------------------------------------------------------------------------------------"
		print "Rank \t Name \t\t\t     Position\tTeam \t Number of TouchDowns"
		print "----------------------------------------------------------------------------------------"
	if(count <= 20):
		player = data.find('a')
		position = data.findAll('td')[1]
		team = (data.findAll('td')[2]).find('a')
		touchdown = data.findAll('td')[6]
		print str(count) + '\t' + player.contents[0].strip() + '\t\t\t' + position.contents[0].strip() + '\t'+ team.contents[0].strip() + '\t\t' + touchdown.contents[0].strip()
	else: exit()	
	

	