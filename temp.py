from gmplot import gmplot
import flavortown_scraper

# Place map
gmap = gmplot.GoogleMapPlotter(37.09024, -95.712891, 4)

#hidden_gem_lat, hidden_gem_lon = 37.770776, -122.461689
#gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')
address_list = flavortown_scraper.get_addresses()
#for address in address_list[3]:
 #   print(address)
    
for address in address_list[6]:
    hidden_gem_lat, hidden_gem_lon = gmap.geocode(address[0])
    gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue', title=address[1])
#print(address)

# Draw
gmap.draw("my_map.html")
 
