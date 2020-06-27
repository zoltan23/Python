from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

def scrapeRoster(my_url):
    team_name = re.search('/fbs/(.*)/roster', my_url).group(1)
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

    player_data = open("/Users/tim/Desktop/Python/LSU Webmap/Data Sets/" + team_name + "_roster.csv", "w")
    player_data.write("name*city*height*weight*position*team\n")

    for name, city, height, weight, position in zip(names, cities, heights, weights, positions):
        name = name.text
        city = city.text
        height = height.text
        weight = weight.text
        position = position.find("div", {"class": "td w8 rostercell_pos hidden-xs"}).text
        team = team_name
        player_data.write(name + "*" + city + "*" + height + "*" + weight + "*" + position + "*" + team + "\n")
        #print(name, city, height, weight, position)

    player_data.close()

