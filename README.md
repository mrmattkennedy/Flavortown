I made this website because I watched too much Diners, Drive-Ins and Dives for a week and wanted to see where the food shows had been.

##Data
All the addresses, shows, restaurants, etc I got from https://www.tvfoodmaps.com/. Follow the links and you can find a list for ~50 shows.
I did some scraping off each show's page, and now there are over 6,000 markers on a single google map, which is why this website is so slow (also this is a [known issue](https://issuetracker.google.com/issues/35820227)

##Requirements
[gmplot](https://pypi.org/project/gmplot/) I have attached a copy of my own gmplot file that has a few changes. The only change that is required is the change in pathing for *self.coloricon*.
[lxml](https://lxml.de/installation.html)
[BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
[requests](https://pypi.org/project/requests/)