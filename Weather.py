import requests
from bs4 import BeautifulSoup

while True:
    # Ask Location
    user_Input = input(
        "Enter the name of the city\n")
    URL = "https://weather.gc.ca/city/jump_e.html?city="+user_Input+"&lang=e"

    # Access Weather Data
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    # If there is multiple option avaliable or city name is invalid
    if soup.find("h1").get_text() == "Change city result":
        print(soup.find("label", {"accesskey": "g"}).get_text())
        # If city name is invalid
        if str(soup.find("main", class_="container")).find("No match found for") != -1:
            print("Input is invalid")
        else:
            x = []
            x = soup.find_all("ul")[3].findChildren()
            del x[::2]
            for i in range(len(x)):
                print(str(i+1)+". "+x[i].get_text())
            # Get input until valid option is given
            while True:
                try:
                    # Show options for cities
                    user_Input = x[int(
                        input("Select from the options above\n"))-1].get_text()
                    URL = "https://weather.gc.ca/city/jump_e.html?city="+user_Input+"&lang=e"
                    page = requests.get(URL)
                    soup = BeautifulSoup(page.content, 'html.parser')
                except:
                    print("Input is invalid\nPlease Try Again")
                    continue
                break
            break
        continue
    else:
        break

# Get location and temperature
try:
    location = soup.find("h1", id="wb-cont").get_text()
    temp = soup.find("span", class_="wxo-metric-hide").get_text()
    print("\n"+location.rstrip())
    print(temp)
except:
    print("Temperature is currently unavaliable at this location")

# Get Condition
try:
    x = soup.find("dl", class_="dl-horizontal wxo-conds-col1")
    x = x.find_all("dd")
    print("Condition: ", x[0].get_text())
    print("Pressure: " + x[1].get_text().rstrip())
    print("Tendency: ", x[3].get_text())

except:
    print("Condition is currently unavaliable at this location")
