from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSfgDEE2vh6p7GHZrBHwAMr7qd8tmEa7ra8OU4izzfO4_PUexA/viewform?' \
           'usp=sf_link'
URL = 'https://www.zameen.com/Rentals/Karachi_DHA_Defence-213-1.html'

request = requests.get(URL)
request.raise_for_status()
WEBSITE = request.text

soup = BeautifulSoup(WEBSITE, 'html.parser')

# Finding Link
link_l = soup.find_all('a', class_='_7ac32433')
link_l = [link.get('href') for link in link_l if link is not None]
links = []
for link in link_l:
    label = 'https://www.zameen.com/'
    links.append(label + link)

# Finding Address
address_l = soup.find_all('div', class_='_162e6469')
address_l = [address.getText() for address in address_l if address is not None]

# Finding Prices
prices_l = soup.find_all('span', class_='f343d9ce')
prices_l = [price.getText() for price in prices_l if price is not None]

# Filling The Form With Selenium
WEB_DRIVER_PATH = Service("D:\Coding\Web Dev Thingies\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=WEB_DRIVER_PATH)

for _ in range(len(links)):
    driver.get(FORM_URL)
    time.sleep(3)

    # Keying in the Address input
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                                  '1]/div/div[1]/input')
    address_input.send_keys(address_l[_])
    # Keying in the Link input
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/'
                                               'div/div[1]/input')
    link_input.send_keys(links[_])
    # Keying in the Prices input
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/'
                                                'div/div[1]/input')
    price_input.send_keys(prices_l[_])

    # Pressing Submit
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

    time.sleep(3)
