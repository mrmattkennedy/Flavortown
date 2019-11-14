import os
import sys
import time
from gmplot import gmplot
import flavortown_scraper

start_time = time.time()


#key = [line.rstrip('\n') for line in open(key_location, 'r')][0]
key_path = sys.path[0] + "\\api.txt"
key = [line.rstrip('\n') for line in open(key_path, 'r')][0]
marker_path = sys.path[4]
marker_path = os.path.join(marker_path, 'Lib\\site-packages\\')
for item in os.listdir(marker_path):
    if 'gmplot' in item:
        marker_path = os.path.join(marker_path, item + '\markers')
        break

if not os.path.isdir(marker_path):
    print("Can't find path to markers")

every_other_marker = ['#' + color[:-4] for color in os.listdir(marker_path)[::2]]
   
# Place map
gmap = gmplot.GoogleMapPlotter(37.09024, -95.712891, 4, apikey=key)
address_list, shows = flavortown_scraper.get_addresses()

color_index = 0;
print('here')
for show_index in range(len(address_list)):
    for address in address_list[show_index]:
        try:
            hidden_gem_lat, hidden_gem_lon = gmap.geocode(address[0])
            show_title = "Name: " + address[1] + "<br>Show: " + shows[show_index]
            gmap.marker(hidden_gem_lat, hidden_gem_lon, color=every_other_marker[color_index], title=show_title)
        except Exception:
            print(address)
            continue
    color_index+=1
    
for color in every_other_marker:
    print(color)

# Draw
gmap.draw("my_map.html")
print("--- %s seconds ---" % (time.time() - start_time))
