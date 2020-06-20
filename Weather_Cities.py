import requests
from bs4 import BeautifulSoup

# Scraping Data (It only has Cities from Ontario)
URL = "https://weather.gc.ca/forecast/canada/index_e.html?id=ON"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
list = soup.find("ul", "list-unstyled col-sm-4")
list = list.findChildren()

# Make a dictionary of cities
list_city = dict()

# Delete duplicate elements
del list[::2]

# Set name as position and link as value
for city in list:
    list_city[city.text] = "https://weather.gc.ca"+str(city.get("href"))

print(list_city["Barrie"])
