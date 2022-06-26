import sys
import os
import random
import re
from datetime import date
import time

import smtplib
import ssl

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtCore import QTimer, QTime, QDate
from MainWindow import Ui_MainWindow
from TimeWidget import TimeWidget

# TODO: Check if trailer tickbox is ticked
# TODO: Get moving back and forth through the app work
# TODO: Perhaps change parameters along with the user?
# TODO: Handle the case when there are no departures
# TODO: Implement global timerange
# TODO: "Reset to any-departure-time" ?
# TODO: Ask user to wait while departure times load
# TODO: Set up mailing stuff
# TODO: Integers in variables.txt


class KombardoPinger(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set up main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Kombardo Pinger")

        # Read variables
        self.var = {}
        with open('variables.txt') as v:
            for line in v:
                (key, val) = line.split()
                self.var[key] = val

        # Set up date screen
        self.loadPageDate()

        # Events (datepage)
        self.ui.pushButton_datenext.clicked.connect(self.dateNext)
        self.ui.dateEdit_first.dateChanged.connect(self.fixLastDate)
        self.ui.dateEdit_last.dateChanged.connect(self.fixFirstDate)

        # Events (timepage)
        self.ui.pushButton_timeprev.clicked.connect(self.timePrev)
        self.ui.pushButton_timenext.clicked.connect(self.timeNext)
        self.ui.pushButton_nextdate.clicked.connect(self.nextDate)
        self.ui.pushButton_prevdate.clicked.connect(self.prevDate)
        self.ui.dateEdit_time.dateChanged.connect(self.changeTimeWidget)

        # Events (notipage)
        self.ui.pushButton_notiprev.clicked.connect(self.notiPrev)
        self.ui.pushButton_search.clicked.connect(self.notiSearch)

        # Events (searchpage)
        self.ui.pushButton_extend.clicked.connect(self.extendTime)
        self.ui.pushButton_end.clicked.connect(self.endSearch)

    def rand_sleep(self, sec, u=0.2):
        noise = random.random()*2 - 1
        time.sleep(sec + sec*u*noise)

    def wait_for_elem(self, xpath, timeout=20, wait=0):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="booking"]/' + xpath)))
        self.rand_sleep(wait)

    def getElement(self, xpath, timeout=20, wait=0):
        self.rand_sleep(wait)
        button = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="booking"]/' + xpath)))
        return button

    def getElements(self, xpath, timeour=20, wait=0):
        self.rand_sleep(wait)
        return self.driver.find_elements(By.XPATH, '//*[@id="booking"]/' + xpath)

    def clickButton(self, button, timeout=20, wait=0):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(button))
        self.rand_sleep(wait)
        button.click()

    def getDepTimes(self, deps):
        deps_times = []
        for dep in deps:
            deps_times.append(dep.find_element(
                By.XPATH, 'div/button/button/div[1]/div[1]/div[2]').text)
        return deps_times
    
    def getAvailable(self, deps):
        # Last piece of text is 'Udsolgt' if tickets are unavailable
        return [dep.text.split()[-1] != 'Udsolgt' for dep in deps]

    def loadPageDate(self):
        self.ui.dateEdit_first.setDate(date.today())
        self.ui.dateEdit_first.setMinimumDate(date.today())
        self.ui.dateEdit_last.setDate(date.today())
        self.ui.dateEdit_last.setMinimumDate(date.today())

        # Open website
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.bornholmslinjen.dk/booking')

        # Decline unnecessary cookies
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'declineButton')))
        #button = 'declineButton'
        #self.wait_for_elem(By.ID, button)
        self.driver.find_element(By.XPATH, '//*[@id="declineButton"]').click()

    def dateNext(self):
        # Save info
        route = self.ui.comboBox_route.currentText().split('-')
        self.orig = route[0]
        self.dest = route[1]

        self.trailer = self.ui.comboBox_trailer.currentText()

        self.n_passengers = self.ui.spinBox_passengers.value()

        self.first_date = self.ui.dateEdit_first.date()
        self.last_date = self.ui.dateEdit_last.date()
        delta = self.first_date.daysTo(self.last_date)
        self.n_dates = delta + 1

        # Fill in website form

        # Origin
        button = self.getElement('div/form/div/div[3]/div[1]/button')
        self.clickButton(button)

        self.rand_sleep(0.5)
        buttons = self.getElements(
            'div/form/div/div[3]/div[1]/div/div/div/div/div/button')
        enum = enumerate(buttons)
        # Dictionary from origin name to button index
        orig_dict = dict((button.text, idx) for idx, button in enum)
        self.clickButton(buttons[orig_dict[self.orig]])

        # Destination
        button = self.getElement('div/form/div/div[3]/div[2]/button')
        self.clickButton(button)

        self.rand_sleep(0.5)
        buttons = self.getElements(
            'div/form/div/div[3]/div[2]/div/div/div/div/div/button')
        enum = enumerate(buttons)
        dest_dict = dict((button.text, idx) for idx, button in enum)
        self.clickButton(buttons[dest_dict[self.dest]])

        # Passengers
        field = self.getElement(
            'div/form/div[3]/div/div[2]/div/div[3]/div/div/div/input')
        field.send_keys(Keys.BACKSPACE)
        field.send_keys(self.ui.spinBox_passengers.value())

        # Trailer
        if self.ui.comboBox_trailer.currentIndex() > 0:
            # Tick checkbox
            button = self.getElement(
                'div/form/div[3]/div/div[2]/div/div[2]/button')
            self.clickButton(button)

            # Select trailer
            buttons = self.getElements(
                'div/form/div[3]/div/div[2]/div/div[3]/div[2]/div/div/button', wait=1)
            self.clickButton(
                buttons[self.ui.comboBox_trailer.currentIndex()-1])

        # Next page
        button = self.getElement('div/form/div[3]/div/button')
        self.clickButton(button)

        # Load time page
        self.loadPageTime(0)
        self.ui.stackedWidget.setCurrentIndex(1)
        # /html/body/div[2]/div/div/section/div/

    def loadPageTime(self, date_idx):
        self.ui.dateEdit_time.setDate(self.ui.dateEdit_first.date())
        self.ui.dateEdit_time.setMinimumDate(self.ui.dateEdit_first.date())
        self.ui.dateEdit_time.setMaximumDate(self.ui.dateEdit_last.date())

        # Get some data on relevant dates
        day_diff = QDate.currentDate().daysTo(self.first_date)
        now_dow = QDate.currentDate().dayOfWeek()
        self.first_dow = self.first_date.dayOfWeek()
        self.last_dow = self.last_date.dayOfWeek()
        week_diff = int((day_diff + now_dow - 1)/7)

        # Switch to weekly view instead of biweekly
        button = self.getElement('div/form/div/div[3]/div/div/button[' +
                                 str(now_dow) + ']')
        self.clickButton(button)

        # Progress forward to the week matching the first departure date
        forward = self.getElement('div/form/div[1]/div[3]/button')
        for i in range(week_diff):
            self.clickButton(forward)

        # Create a TimeWidget for each departure date
        self.timeWidgets = []
        self.rand_sleep(1)
        dow = self.first_dow
        for i in range(self.n_dates):
            # Progress to next week when needed
            if dow == 8:
                dow -= 7
                self.clickButton(forward)

            # Click on date button to reveal departing times
            button = self.getElement('div/form/div[1]/div[2]/div/div/button[' +
                                     str(dow) + ']')
            self.clickButton(button)
            self.wait_for_elem('div/form/div[3]/div')
            elems = self.getElements('div/form/div')[2:]
            dep_times = self.getDepTimes(elems)
            available = self.getAvailable(elems)

            self.timeWidgets.append(TimeWidget(elems, dep_times, available))

            dow += 1

        # Create a stackedwidget page for each date (after removing the existing stackedwidget)
        self.ui.time_layout.removeWidget(
            self.ui.time_layout.itemAt(2).widget())
        self.ui.stackedWidget_time = QStackedWidget()
        self.ui.time_layout.insertWidget(2, self.ui.stackedWidget_time)
        for w in self.timeWidgets:
            self.ui.stackedWidget_time.addWidget(w)

    def timePrev(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def timeNext(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def fixLastDate(self):
        if self.ui.dateEdit_first.date() > self.ui.dateEdit_last.date():
            self.ui.dateEdit_last.setDate(self.ui.dateEdit_first.date())

    def fixFirstDate(self):
        if self.ui.dateEdit_first.date() > self.ui.dateEdit_last.date():
            self.ui.dateEdit_first.setDate(self.ui.dateEdit_last.date())

    def nextDate(self):
        self.ui.dateEdit_time.setDate(
            self.ui.dateEdit_time.date().addDays(1))

    def prevDate(self):
        self.ui.dateEdit_time.setDate(
            self.ui.dateEdit_time.date().addDays(-1))

    def changeTimeWidget(self):
        idx = self.first_date.daysTo(self.ui.dateEdit_time.date())
        self.ui.stackedWidget_time.setCurrentIndex(idx)

        # Disable left/right buttons as needed
        self.ui.pushButton_nextdate.setEnabled(True)
        self.ui.pushButton_prevdate.setEnabled(True)

        if idx == 0:
            self.ui.pushButton_prevdate.setEnabled(False)

        if idx == self.n_dates - 1:
            self.ui.pushButton_nextdate.setEnabled(False)

    def notiPrev(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def notiSearch(self):
        # Check validity of mail
        mail = self.ui.lineEdit_mail.text()

        mail_split = mail.split('@')
        if len(mail_split) != 2:
            return

        mail_split_split = mail_split[1].split('.')
        if len(mail_split_split) < 2:
            return
        if not all(len(s) > 0 for s in mail_split_split):
            return

        self.ui.stackedWidget.setCurrentIndex(3)
        self.start_time = QTime.currentTime()
        self.end_time =  self.start_time.addSecs(50)
        self.startSearchLoop()
    
    def extendTime(self):
        self.end_time = self.end_time.addSecs(20)
        self.ui.pushButton_extend.setEnabled(False)
        
        # Update search-end time text
        text = self.ui.label_endTime.text()
        end_time = self.end_time.toString('hh:mm')
        text = re.sub('..:..', end_time, text)
        self.ui.label_endTime.setText(text)

    def endSearch(self):
        self.driver.close()
        self.close()
        
    def startSearchLoop(self):
        # Display search-end time text
        text = self.ui.label_endTime.text()
        end_time = self.end_time.toString('hh:mm')
        text = re.sub('..:..', end_time, text)
        self.ui.label_endTime.setText(text)
        
        # Print currently available departures
        date = self.first_date
        
        for i in range(self.n_dates):
            print(date)
            print(self.timeWidgets[i].available)
            date = date.addDays(1)
        
        self.searchLoop()

    def searchLoop(self):
        time_until_end = QTime.currentTime().secsTo(self.end_time)
        if time_until_end > 0:
            print(time_until_end)
            if time_until_end < 20:
                self.ui.pushButton_extend.setEnabled(True)
            QTimer.singleShot(5000, self.searchLoop)
        else:
            self.endSearch()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = KombardoPinger()
    widget.show()
    app.exec_()

# %%

#TODO: GUI
# TODO: Global timeout (to prevent running forever)
# TODO: Take into consideration when a departure time is passed

receiver = 'mads2112@live.dk'
timeout = 20
wait = 1
auto_input = True
input_list = ['Ystad-Rønne', 'Alm', '2', '13', '08:30', '18:30']


def init_email(receiver):
    mail_dict = {}
    with open('variables.txt') as v:
        for line in v:
            (key, val) = line.split()
            mail_dict[key] = val

    mail_dict['receiver'] = receiver
    return mail_dict


def send_mail(mail_dict, departure):
    subject = 'Subject: Ledig billet [dato] kl. ' + departure + '\n\n'
    text = 'Der er kommet ledige billetter til afgangen ' + input_list[0] + \
        'd. ' + input_list[3] + '. kl. ' + departure
    message = subject + text

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(mail_dict['smtp_server'],
                          mail_dict['port'], context=context) as server:
        server.login(mail_dict['sender'], mail_dict['password'])
        server.sendmail(mail_dict['sender'], receiver, message)


def wait_for_elem(driver, by, addr, timeout, wait):
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, addr)))
    rand_sleep(wait)


def rand_sleep(sec, u=0.2):
    noise = random.random()*2 - 1
    time.sleep(sec + sec*u*noise)


def auto_or_input(auto_input, auto):
    if auto_input:
        return auto
    return input()


def is_timed_out():
    return EC.element_to_be_clickable((By.XPATH, '//*[@id="js-booking"]/div/div[2]/div/button[2]'))


# Get email info
mail_dict = init_email(receiver)

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
button_addr = '//*[@id="' + parent + '"]/' + button
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
button_addr = '//*[@id="' + parent + '"]/' + button

wait_for_elem(driver, By.ID, parent, timeout, wait)
driver.find_element(By.XPATH, button_addr).click()

# Trailer
button = 'div/div[2]/ul/li[1]/button'
parent = 'step-trailer'
button_addr = '//*[@id="' + parent + '"]/' + button

wait_for_elem(driver, By.ID, parent, timeout, wait)
driver.find_element(By.XPATH, button_addr).click()

# Number of passengers
print('Hvor mange passagerer? (1-9)')
num = int(auto_or_input(auto_input, input_list[2]))

button = f'div/div[2]/div/div/ul/li[{num}]'
parent = 'step-passengerCar'
button_addr = '//*[@id="' + parent + '"]/' + button

wait_for_elem(driver, By.ID, parent, timeout, wait)
driver.find_element(By.XPATH, button_addr).click()

# Date
button = 'div/div[2]/button/div'
parent = 'step-outbound/date'
button_addr = '//*[@id="' + parent + '"]/' + button

# Seems like actual button isn't loaded as quickly as its parent
wait_for_elem(driver, By.XPATH, button_addr, timeout, wait)
driver.find_element(By.XPATH, button_addr).click()

button = 'div/div[2]/ul/li[1]/button'
button_addr = '//*[@id="' + parent + '"]/' + button
first = int(driver.find_element(By.XPATH, button_addr).text.split('\n')[1])
button = 'div/div[2]/ul/li[28]/button'
button_addr = '//*[@id="' + parent + '"]/' + button
last = int(driver.find_element(By.XPATH, button_addr).text.split('\n')[1])
month_wrap = False
month_last = 31
if first > last:
    month_wrap = True
    month_last = 28 - last + first - 1

if month_wrap:
    print('Vælg en dato mellem ' + str(first) + ' og ' +
          str(month_last) + ' eller 1 og ' + str(last))
else:
    print('Vælg en dato mellem ' + str(first) + ' og ' + str(last))
num = int(auto_or_input(auto_input, input_list[3]))

idx = (num - first + 1) % month_last

button = f'div/div[2]/ul/li[{idx}]/button'
button_addr = '//*[@id="' + parent + '"]/' + button

driver.find_element(By.XPATH, button_addr).click()

# Time
buttons = 'div/div[2]/ul/li'
parent = 'step-outbound/departure'
buttons_addr = '//*[@id="' + parent + '"]/' + buttons

wait_for_elem(driver, By.ID, parent, timeout, wait)

departures = driver.find_elements(By.XPATH, buttons_addr)
dep_times = [dep.text.split('\n')[1] for dep in departures]
print('Mulige afgange:')
for dep_time in dep_times:
    print(dep_time)

print('Hvad er tidligste afganstidspunkt?')
first = dep_times.index(auto_or_input(auto_input, input_list[4]))
print('Hvad er seneste afgangstidspunkt?')
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
# TODO: Implementer button/parent ting her
for i in range(20):
    #driver.find_element(By.XPATH, '//*[@id="js-booking"]/div/div[2]/div/button[2]').click()
    rand_sleep(300)
    print('We gotta go back!')
    #driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[1]/button').click()
    driver.back()
    rand_sleep(5)
    #driver.find_element(By.XPATH, '//*[@id="app-legacy"]/div/div/div/ul/li/div/div[2]/ul/li[1]/button').click()
    driver.forward()
    wait_for_elem(driver, By.ID, parent, timeout, 2)

    new_dep = driver.find_elements(By.XPATH, buttons_addr)
    new_avail = [dep.text.split('\n')[-1] != 'UDSOLGT' for dep in new_dep]

    for j in range(first, last+1):
        if (not available[j]) and new_avail[j]:
            send_mail(mail_dict, dep_times[j])
            print('Der er kommet ledige billetter til afgangen kl. ' +
                  dep_times[j])

    departures = new_dep
    available = new_avail

driver.close()


# Strip this part:
# /html/body/div[3]
