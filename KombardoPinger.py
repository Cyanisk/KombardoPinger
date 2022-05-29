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
#TODO: Click elements when they are ready

timeout = 20
wait = 1
auto_input = True
input_list = ['Rønne-Ystad', 'Alm', '2', '30', '06:30', '16:30']

def wait_for_elem(driver, by, addr, timeout, wait):
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, addr)))
    rand_sleep(wait)

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

# Decline unnecessary cookies
button = 'declineButton'
wait_for_elem(driver, By.ID, button, timeout, wait)
driver.find_element(By.XPATH, '//*[@id="declineButton"]').click()

# Start booking
button = 'div/div[2]/ul/li[1]/button'
parent = 'step-type'
button_addr = '//*[@id="' + parent +'"]/' + button
wait_for_elem(driver, By.ID, parent, timeout, wait)
driver.find_element(By.XPATH, button_addr).click()

# Select route
route_dict = {'Rønne-Ystad': ['div/div[2]/div/ul[1]/li[2]/button',
                              'div/div[2]/div/ul[2]/li[2]/button'],
              'Ystad-Rønne': ['div/div[2]/div/ul[1]/li[3]/button',
                              'div/div[2]/div/ul[2]/li[2]/button']}
parent = 'step-route'

print('Hvilken rute? skriv \"Rønne-Ystad\" eller \"Ystad-Rønne\"')
string = auto_or_input(auto_input, input_list[0])

button_addr = '//*[@id="' + parent + '"]/' + route_dict[string][0]
wait_for_elem(driver, By.ID, parent, timeout, wait)
driver.find_element(By.XPATH, button_addr).click()

rand_sleep(1)

button_addr = '//*[@id="' + parent + '"]/' + route_dict[string][1]
driver.find_element(By.XPATH, button_addr).click()


# Ticket type
type_dict = {'Alm': 'div/div[2]/ul/li[1]/button',
             'Pensionist': 'div/div[2]/ul/li[2]/button'}
parent = 'step-transportGroups'

print('Hvilken type? skriv \"Alm\" eller \"Pensionist\"')
string = auto_or_input(auto_input, input_list[1])

button_addr = '//*[@id="' + parent + '"]/' + type_dict[string]
wait_for_elem(driver, By.ID, parent, timeout, wait)
driver.find_element(By.XPATH, button_addr).click()

# Means of transport
button = 'div/div[2]/ul/li[1]/button'
parent = 'step-transport'
button_addr = '//*[@id="' + parent +'"]/' + button

wait_for_elem(driver, By.ID, parent, timeout, wait)
driver.find_element(By.XPATH, button_addr).click()

#WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, 'step-transport')))
#rand_sleep(1)
#driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li[2]/div/div[2]/ul/li[1]/button').click()
#rand_sleep(4)

# Trailer
button = 'div/div[2]/ul/li[1]/button'
parent = 'step-trailer'
button_addr = '//*[@id="' + parent +'"]/' + button

wait_for_elem(driver, By.ID, parent, timeout, wait)
driver.find_element(By.XPATH, button_addr).click()

#WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, 'step-trailer')))
#rand_sleep(1)
#driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[1]/button').click()
#rand_sleep(2)

# Number of passengers
print('Hvor mange passagerer? (1-9)')
num = int(auto_or_input(auto_input, input_list[2]))

button = f'div/div[2]/div/div/ul/li[{num}]'
parent = 'step-passengerCar'
button_addr = '//*[@id="' + parent +'"]/' + button

wait_for_elem(driver, By.ID, parent, timeout, wait)
driver.find_element(By.XPATH, button_addr).click()
#num = int(input())

#WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, 'step-passengerCar')))
#rand_sleep(1)
#driver.find_element(By.XPATH, f'//*[@id="app-legacy"]/div/div/div/ul/li[2]/div/div[2]/div/div/ul/li[{num}]/label/span').click()
#rand_sleep(5)

# Date
button = 'div/div[2]/button/div'
parent = 'step-outbound/date'
button_addr = '//*[@id="' + parent +'"]/' + button

# Seems like actual button isn't loaded as quickly as its parent
wait_for_elem(driver, By.XPATH, button_addr, timeout, wait)
driver.find_element(By.XPATH, button_addr).click()

#x_more_dates = '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/button/div'
#WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, x_more_dates)))
#rand_sleep(1)
#driver.find_element(By.XPATH, x_more_dates).click()
#rand_sleep(1)

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

button = f'div/div[2]/ul/li[{idx}]/button'
button_addr = '//*[@id="' + parent +'"]/' + button

driver.find_element(By.XPATH, button_addr).click()

#driver.find_element(By.XPATH, f'//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[{idx}]/button').click()
#rand_sleep(5)

# Time
buttons = 'div/div[2]/ul/li'
parent = 'step-outbound/departure'
buttons_addr = '//*[@id="' + parent +'"]/' + buttons

wait_for_elem(driver, By.ID, parent, timeout, wait)

#WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, 'step-outbound/departure')))
#rand_sleep(1)

departures = driver.find_elements(By.XPATH, buttons_addr)
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
#TODO: Implementer button/parent ting her
webdriver.ActionChains(driver).move_to_element(departures[0]).perform()
for i in range(20):
    #/html/body/div[3]/div/div/div/div[2]/div
    #/html/body/div[3]/div/div/div/div[2]/div/button[2]
    rand_sleep(300)
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