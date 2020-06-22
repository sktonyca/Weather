import requests
from bs4 import BeautifulSoup

# Call the scarp function to retrieve cities
#list_city = scarpData()

# Ask Location

user_Input = input(
    "Enter the name of the city \nei) City, Province Abbreviation\n")
URL = "https://weather.gc.ca/city/jump_e.html?city="+user_Input+"&lang=e"

# Access Weather Data
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Get Location
location = soup.find("h1", id="wb-cont").get_text()

# Get Temperature
try:
    temp = soup.find("span", class_="wxo-metric-hide").get_text()
    print(temp)
except:
    print("Temperature is currently unavaliable at this location")

# Get Condition
try:
    condition = soup.find("dd", class_="mrgn-bttm-0").get_text()
except:
    print("Condition is currently unavaliable at this location")
