import requests
from bs4 import BeautifulSoup

# Ask Location
user_Input = input(
    "Enter the name of the city\n")
URL = "https://weather.gc.ca/city/jump_e.html?city="+user_Input+"&lang=e"

# Access Weather Data
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# If there is multiple option avaliable
if soup.find("label", {"accesskey": "g"}).get_text() != None:
    x = []
    x = soup.find_all("ul")[3].findChildren()
    del x[::2]
    for i in range(len(x)):
        print(i+1, x[i].get_text())
    # Get input until valid option is given
    while True:
        try:
            user_Input = x[int(
                input("Select from the options above\n"))-1].get_text()
            URL = "https://weather.gc.ca/city/jump_e.html?city="+user_Input+"&lang=e"
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
        except:
            print("Input is invalid\nPlease Try Again")
            continue
        break

# Get Location
location = soup.find("h1", id="wb-cont").get_text()
print(location)

# Get Temperature
try:
    temp = soup.find("span", class_="wxo-metric-hide").get_text()
    print(temp)
except:
    print("Temperature is currently unavaliable at this location")

# Get Condition
# try:
    #condition = soup.find("dd", class_="mrgn-bttm-0").get_text()
# except:
    #print("Condition is currently unavaliable at this location")
