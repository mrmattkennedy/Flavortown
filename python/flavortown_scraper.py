import requests
import copy
import re
from lxml import html
from bs4 import BeautifulSoup

#Need to get info on restaurants for markers, as well as show title
#Do it as a 3d list, parse for title in beginning
def get_addresses():
    #Starting point: get the show list from here
    page = requests.get('https://www.tvfoodmaps.com/T_TVShows.jsp')
    webpage = html.fromstring(page.content)

    #Get a list of all the shows
    shows = []
    for link in webpage.xpath('//a/@href'):
        if link.startswith("/show") and not any(link in existing_link for existing_link in shows):
            shows.append(link)

    #Append the rest of the link to the shows
    show_names = [show[len('/show/'):].replace('-', ' ') for show in shows]
    #print(show_names)
    shows = ["https://www.tvfoodmaps.com" + show + "/all" for show in shows]

    #Get all addresses listed in all shows
    addresses = []
    address_beginner = '[<p class="searchResAddress">'
    address_end = '</p>]'
    name_beginner = '<h3 style="display:inline"><a href='
    name_end = '</a> </h3>]'
    phone_regex = "\(\w{3}\) \w{3}-\w{4}"
    
    for show in shows:
        #Get a link to the show page
        show_link = requests.get(show)
        #Parse with beautifulsoup
        soup = BeautifulSoup(show_link.content.decode("utf-8", errors='ignore'),'html.parser')
        #Get a list of all restaurants
        restaurants = soup.findAll("div", {"class": "inner-results"})
        
        #Get the addresses specifically, then clean them up
        names = [str(restaurant.findAll("h3", {"style": "display:inline"})) for restaurant in restaurants]
        names = [name[name.find('>', len(name_beginner)) + 1:len(name) - len(name_end)] for name in names]
        
        temp_addresses = [str(restaurant.findAll("p", {"class": "searchResAddress"})) for restaurant in restaurants]
        temp_addresses = [address[len(address_beginner):len(address) - len(address_end)] for address in temp_addresses]
        temp_addresses = [re.sub(phone_regex, '', address) for address in temp_addresses]

        #Combine lists, map them as lists in a list with list comprehension
        temp = [list(info) for info in zip(temp_addresses, names)]
        addresses.append(copy.deepcopy(temp))


    #Sometimes there is no address, which means just remove it
    for address_list in addresses:
        for address in address_list:
            if address[0].startswith(' ') and not address[0][1].isdigit():
                address_list.remove(address)
            if address[0].startswith('Mobile'):
                address_list.remove(address)

    shows = [show[len('https://www.tvfoodmaps.com/show/'):len(show) - len('/all')].replace('-', ' ') for show in shows]
    return addresses, shows

#temp = get_addresses()

#print(len(temp))
#print(len(temp[0]))
#print(temp[3])
#print(temp)
