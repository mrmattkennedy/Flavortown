import requests
import copy
from lxml import html
from bs4 import BeautifulSoup

page = requests.get('https://www.tvfoodmaps.com/T_TVShows.jsp')
webpage = html.fromstring(page.content)

#Get a list of all teh shows
shows = []
for link in webpage.xpath('//a/@href'):
    if link.startswith("/show") and not any(link in existing_link for existing_link in shows):
        shows.append(link)

#Append the rest of the link to the shows
shows = ["https://www.tvfoodmaps.com" + show + "/all" for show in shows]

#Get all addresses listen in all shows
addresses = []
for show in shows:    
    show_link = requests.get(show)
    soup = BeautifulSoup(show_link.content.decode("utf-8", errors='ignore'),'html.parser')
    restaurants = soup.findAll("div", {"class": "inner-results"})
    temp = [str(restaurant.findAll("p", {"class": "searchResAddress"})) for restaurant in restaurants]
    print(len(temp))
    addresses.append(copy.deepcopy(temp))

print("Addresses is " + str(len(addresses)))
#tags = [str(tag) for tag in tags]
