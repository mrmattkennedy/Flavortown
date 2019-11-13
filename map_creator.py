import os
import sys
import time
from gmplot import gmplot
import flavortown_scraper

start_time = time.time()

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
gmap = gmplot.GoogleMapPlotter(37.09024, -95.712891, 4)

#hidden_gem_lat, hidden_gem_lon = 37.770776, -122.461689
#gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')
address_list = flavortown_scraper.get_addresses()
#for address in address_list[3]:
 #   print(address)


color_index = 0;
for show in address_list:
    for address in show:
        try:
            hidden_gem_lat, hidden_gem_lon = gmap.geocode(address[0])
            gmap.marker(hidden_gem_lat, hidden_gem_lon, color=every_other_marker[color_index], title=address[1])
        except Exception:
            print(address)
            continue
    color_index+=1
    
#print(address)

# Draw
gmap.draw("my_map.html")
print("--- %s seconds ---" % (time.time() - start_time))
