from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


# return a value in [sec*(1-u); sec*(1+u)]
def rand_time(sec, u=0.2):
    noise = random.random()*2 - 1
    return sec + sec*u*noise

# Open website
driver = webdriver.Firefox()
driver.get('https://www.bornholmslinjen.dk/booking#type')
time.sleep(rand_time(2))

# Decline extra cookies
driver.find_element(By.XPATH, '//*[@id="declineButton"]').click()
time.sleep(rand_time(1))

# Start booking
driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[1]/button').click()

# Select route
route_dict = {'Rønne-Ystad': ['//*[@id="app-legacy"]/div/div/div/ul/li[2]/div/div[2]/div/ul[1]/li[2]/button',
                              '//*[@id="app-legacy"]/div/div/div/ul/li[2]/div/div[2]/div/ul[2]/li[2]/button'],
              'Ystad-Rønne': ['//*[@id="app-legacy"]/div/div/div/ul/li[2]/div/div[2]/div/ul[1]/li[3]/button',
                              '//*[@id="app-legacy"]/div/div/div/ul/li[2]/div/div[2]/div/ul[2]/li[2]/button']}

print('Hvilken rute? skriv \"Rønne-Ystad\" eller \"Ystad-Rønne\"')
string = input()

driver.find_element(By.XPATH, route_dict[string][0]).click()
time.sleep(rand_time(1))
driver.find_element(By.XPATH, route_dict[string][1]).click()

# Ticket type
type_dict = {'Alm': '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[1]/button',
             'Pensionist': '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[2]/button'}

print('Hvilken type? skriv \"Alm\" eller \"Pensionist\"')
string = input()

driver.find_element(By.XPATH, type_dict[string]).click()
time.sleep(rand_time(1))

# Means of transport
driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li[2]/div/div[2]/ul/li[1]/button').click()
time.sleep(rand_time(2))

# Trailer
driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[1]/button').click()

# Number of passengers
print('Hvor mange passagerer? (1-9)')
num = int(input())

driver.find_element(By.XPATH, f'//*[@id="app-legacy"]/div/div/div/ul/li[2]/div/div[2]/div/div/ul/li[{num}]/label/span').click()
time.sleep(rand_time(5))

# Date
driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/button/div').click()
time.sleep(rand_time(1))

first = int(driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[1]/button').text.split('\n')[1])
last = int(driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[28]/button').text.split('\n')[1])
month_wrap = False
month_last = 31
if first > last:
    month_wrap = True
    month_last = 28- last + first - 1

if month_wrap:
    print('Vælg en dato mellem ' + str(first) + ' og ' + str(month_last) + ' eller 1 og ' + str(last))
else:
    print('Vælg en dato mellem ' + str(first) + ' og ' + str(last))
num = int(input())
idx = (num - 28 + 2) % month_last

driver.find_element(By.XPATH, f'//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[{idx}]/button').click()
time.sleep(rand_time(2))

# Time
departures = driver.find_elements(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li')
dep_times = [dep.text.split('\n')[1] for dep in departures]
print('Mulige afgange:')
for dep_time in dep_times:
    print(dep_time)

print('Hvad er tidligste afganstidspunkt?')
first = dep_times.index(input())
print('Hvad er seneste afgangstidspunkt?')
last = dep_times.index(input())

available = [dep.text.split('\n')[-1] != 'UDSOLGT' for dep in departures]

has_available = False
for i in range(len(departures)):
    if available[i]:
        if not has_available:
            has_available = True
            print('På nuværende tidspunkt har disse afgange ledige billetter:')
        print(dep_times[i])

#driver.close()

# Strip this part:
#/html/body/div[3]