import requests
from bs4 import BeautifulSoup
from Weather_Cities import scarpData

# Call the scarp function to retrieve cities
list_city = scarpData()

# Ask Location
correct = False
while correct == False:
    user_Input = input("Enter the name of the city\n").title()
    if user_Input not in list_city:
        print("It is not a valid city")
        continue
    break

# Access Weather Data
page = requests.get(list_city[user_Input])
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
