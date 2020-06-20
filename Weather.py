import requests
from bs4 import BeautifulSoup
from Weather_Cities import list_city

# Scraping Data
#URL = "https://weather.gc.ca/city/pages/on-118_metric_e.html"
#page = requests.get(URL)
#soup = BeautifulSoup(page.content, 'html.parser')

# Get Location
#location = soup.find("h1", id="wb-cont")
#location = location.get_text()

# Get Temperature
#temp = soup.find("span", class_="wxo-metric-hide")
#temp = temp.get_text()

# Print the retrieved value
#print(location + temp)


correct = False
while correct == False:
    user_Input = input("Enter the name of the city\n")
    if user_Input not in list_city:
        print("It is not a valid city")
        continue
    break

# Access Weather Data
page = requests.get(list_city[user_Input])
soup = BeautifulSoup(page.content, 'html.parser')

# Get Location
location = soup.find("h1", id="wb-cont")
location = location.get_text()

# Get Temperature
temp = soup.find("span", class_="wxo-metric-hide")
temp = temp.get_text()

# Print the retrieved value
print(location + temp)
