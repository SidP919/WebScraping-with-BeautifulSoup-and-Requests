import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09979000000004&lon=-118.32721499999997#.XiBgC8gzbIU')
soup = BeautifulSoup(page.content, 'html.parser')
#soup is the string containing the whole source code of the webpage

week = soup.find(id="seven-day-forecast-body")
items = week.find_all(class_='tombstone-container')
# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]

# print(period_names)
# print(short_desc)
# print(temp)

#Using Panda library to format the data in a better way:------------->>>>
weather_data = pd.DataFrame(
  {
    'period':period_names,
    'short_description': short_desc,
    'temperature': temp
  }
)
print(weather_data)

#Panda also let's you create a csv file onto your computer filled with desired data
weather_data.to_csv('weather.csv')