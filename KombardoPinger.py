from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

#TODO: GUI
#TODO: Booking times out after 20 minutes. Start anew when this happens
#TODO: Notification stuff

auto_input = True
input_list = ['Rønne-Ystad', 'Alm', '2', '29', '06:30', '16:30']

# return a value in [sec*(1-u); sec*(1+u)]
def rand_sleep(sec, u=0.2):
    noise = random.random()*2 - 1
    time.sleep(sec + sec*u*noise)

def auto_or_input(auto_input, auto):
    if auto_input:
        return auto
    return input()

# Open website
driver = webdriver.Firefox()
driver.get('https://www.bornholmslinjen.dk/booking#type')
rand_sleep(2)

# Decline extra cookies
driver.find_element(By.XPATH, '//*[@id="declineButton"]').click()
rand_sleep(1)

# Start booking
driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[1]/button').click()
rand_sleep(1)

# Select route
route_dict = {'Rønne-Ystad': ['//*[@id="app-legacy"]/div/div/div/ul/li[2]/div/div[2]/div/ul[1]/li[2]/button',
                              '//*[@id="app-legacy"]/div/div/div/ul/li[2]/div/div[2]/div/ul[2]/li[2]/button'],
              'Ystad-Rønne': ['//*[@id="app-legacy"]/div/div/div/ul/li[2]/div/div[2]/div/ul[1]/li[3]/button',
                              '//*[@id="app-legacy"]/div/div/div/ul/li[2]/div/div[2]/div/ul[2]/li[2]/button']}

print('Hvilken rute? skriv \"Rønne-Ystad\" eller \"Ystad-Rønne\"')
string = auto_or_input(auto_input, input_list[0])
#string = input()

driver.find_element(By.XPATH, route_dict[string][0]).click()
rand_sleep(1)
driver.find_element(By.XPATH, route_dict[string][1]).click()
rand_sleep(3)

# Ticket type
type_dict = {'Alm': '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[1]/button',
             'Pensionist': '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[2]/button'}

print('Hvilken type? skriv \"Alm\" eller \"Pensionist\"')
string = auto_or_input(auto_input, input_list[1])
#string = input()

driver.find_element(By.XPATH, type_dict[string]).click()
rand_sleep(1)

# Means of transport
driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li[2]/div/div[2]/ul/li[1]/button').click()
rand_sleep(4)

# Trailer
driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[1]/button').click()
rand_sleep(2)

# Number of passengers
print('Hvor mange passagerer? (1-9)')
num = int(auto_or_input(auto_input, input_list[2]))
#num = int(input())

driver.find_element(By.XPATH, f'//*[@id="app-legacy"]/div/div/div/ul/li[2]/div/div[2]/div/div/ul/li[{num}]/label/span').click()
rand_sleep(5)

# Date
driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/button/div').click()
rand_sleep(1)

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
num = int(auto_or_input(auto_input, input_list[3]))
#num = int(input())
idx = (num - first + 1) % month_last

driver.find_element(By.XPATH, f'//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[{idx}]/button').click()
rand_sleep(5)

# Time
departures = driver.find_elements(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li')
dep_times = [dep.text.split('\n')[1] for dep in departures]
print('Mulige afgange:')
for dep_time in dep_times:
    print(dep_time)

print('Hvad er tidligste afganstidspunkt?')
#first = dep_times.index(input())
first = dep_times.index(auto_or_input(auto_input, input_list[4]))
print('Hvad er seneste afgangstidspunkt?')
#last = dep_times.index(input())
last = dep_times.index(auto_or_input(auto_input, input_list[5]))

available = [dep.text.split('\n')[-1] != 'UDSOLGT' for dep in departures]

has_available = False
for i in range(first, last+1):
    if available[i]:
        if not has_available:
            has_available = True
            print('På nuværende tidspunkt har disse afgange ledige billetter:')
        print(dep_times[i])

# Start looping
webdriver.ActionChains(driver).move_to_element(departures[0]).perform()
for i in range(20):
    rand_sleep(100)
    webdriver.ActionChains(driver).move_by_offset(20, 15).perform()
    rand_sleep(100)
    webdriver.ActionChains(driver).move_by_offset(5, -20).perform()
    rand_sleep(100)
    webdriver.ActionChains(driver).move_by_offset(-25, 5).perform()
    driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[1]/button').click()
    #driver.back()
    rand_sleep(5)
    driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[1]/button').click()
    #driver.forward()
    rand_sleep(5)
    
    new_dep = driver.find_elements(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li')
    new_avail = [dep.text.split('\n')[-1] != 'UDSOLGT' for dep in new_dep]
    
    for j in range(first, last+1):
        if (available[j] | new_avail[j]) != available[j]:
            print('Der er kommet ledige billetter til afgangen kl. ' + dep_times[j])
    
    departures = new_dep
    available = new_avail

driver.close()


# Strip this part:
#/html/body/div[3]