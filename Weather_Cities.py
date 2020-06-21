import requests
from bs4 import BeautifulSoup


def scarpData():
    # Scraping Data (It only has Cities from Ontario)
    URL = "https://weather.gc.ca/forecast/canada/index_e.html?id=ON"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    list = soup.find_all("ul", "list-unstyled col-sm-4")

    # Create temperary list
    temp = []

    # Add items to the temperary list
    for x in range(len(list)):
        temp.append(list[x].findChildren())

    # Erase List
    list = None

    # Re-using the list to add all elements into one section
    list = []
    for sublist in temp:
        for item in sublist:
            list.append(item)

    # Erase List
    temp = None

    # Make a dictionary of cities
    list_city = dict()

    # Delete duplicate elements
    del list[::2]
    print(list)

    # Set name as position and link as value
    for city in list:
        list_city[city.text] = "https://weather.gc.ca"+str(city.get("href"))
    return(list_city)


scarpData()
