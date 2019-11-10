from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(37.09024, -95.712891, 4)

hidden_gem_lat, hidden_gem_lon = 37.770776, -122.461689
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

# Draw
gmap.draw("my_map.html")
