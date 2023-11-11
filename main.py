from bs4 import BeautifulSoup;
from selenium import webdriver;
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import re
from geopy.geocoders import Nominatim

options = Options();
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service('C:/Users/Andrei/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.boat24.com/en/secondhandboats/?src=lagoon&cat=&whr=EUR&prs_min=&prs_max=&lge_min=&lge_max=&bre_min=&bre_max=&jhr_min=&jhr_max=&sort=rand'
driver.get(url)

f = open('./locations.csv', 'w+', encoding="utf-8", newline='')
writer = csv.writer(f)

soup = BeautifulSoup(driver.page_source, 'html.parser')
items = soup.find_all('div', {'class': 'blurb'})
for item in items:
    current_row = []

    title = item.find('h3', {'class': 'blurb__title'}).getText()
    current_row.append(title)

    location = item.find('p', {'class': 'blurb__location'}).getText().replace('» ', '')
    current_row.append(location)
    geolocator = Nominatim(user_agent='VSCode')
    geo_result = geolocator.geocode(location)
    if geo_result : print(geo_result.latitude)

    price_str = item.find('p', {'class': 'blurb__price'}).getText().replace('.', '')
    price = int(re.search(r'\d+', price_str)[0])
    current_row.append(price)

    writer.writerow(current_row)

f.close()
