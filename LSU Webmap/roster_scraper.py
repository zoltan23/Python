from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://www.footballdb.com/college-football/teams/fbs/lsu/roster'
     
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

roster = page_soup.find("div", {"class": "divtable"})

names = roster.find_all('a')
cities = roster.find_all("div", {"class": "td w40 rostercell_coll hidden-xs"})
heights = roster.find_all("div", {"class": "td w8 rostercell_ht hidden-xs"})
weights = roster.find_all("div", {"class": "td w8 rostercell_wt hidden-xs"})
positions = roster.find_all("div", {"class": "tr"})

 
for name, city, height, weight, position in zip(names, cities, heights, weights, positions):
    name = name.text
    city = city.text
    height = height.text
    weight = weight.text
    position = position.find("div", {"class": "td w8 rostercell_pos hidden-xs"}).text
    print(name, city, height, weight, position)




