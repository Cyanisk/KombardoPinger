import sys
import traceback
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
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtCore import QTimer, QTime, QDate, QDateTime
from MainWindow import Ui_MainWindow
from TimeWidget import TimeWidget

# TODO: Perhaps change parameters along with the user?
# TODO: Try to leave more room for user input while working?
# TODO: Use timeout in getElements
# TODO: Maybe put more variables in the GUI?
# TODO: Rename functions?
# TODO: A function handling exceptions
# TODO: Hide browser
# TODO: Handle when geckodriver wants to update (program crashes)

def loading_is_done(locator):
    """ Custom ExpectedCondition for determining whether the element is no
    longer present"""
    
    def _predicate(driver):
        try:
            driver.find_element(*locator)
        except NoSuchElementException:
            return driver.find_element(By.XPATH, '//*[@id="booking"]')
        else:
            raise NoSuchElementException
    
    return _predicate

class KombardoPinger(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set up main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Kombardo Pinger")
        
        # Number of exceptions since last succesful search iteration
        self.exception_streak = 0

        # Read variables
        self.var = {}
        with open('variables.txt') as v:
            for line in v:
                (key, val) = line.split()
                self.var[key] = val
        
        # Convert some variables to ints
        v_list = ['init_search_hours', 'extend_search_hours', 'timeout_secs']
        for v in v_list:
            self.var[v] = int(self.var[v])
        
        self.months = {'Januar':1, 'Februar':2, 'Marts':3, 'April':4,
                       'Maj':5, 'Juni':6, 'Juli':7, 'August':8,
                       'September':9, 'Oktober':10, 'November':11, 'December':12}

        # Set up date screen
        self.loadPageDate()

        # Events (datepage)
        self.ui.pushButton_datenext.clicked.connect(self.dateNext)
        self.ui.dateEdit_first.dateChanged.connect(self.fixLastDate)
        self.ui.dateEdit_last.dateChanged.connect(self.fixFirstDate)

        # Events (timepage)
        self.ui.pushButton_timenext.clicked.connect(self.timeNext)
        self.ui.pushButton_nextdate.clicked.connect(self.nextDate)
        self.ui.pushButton_prevdate.clicked.connect(self.prevDate)
        self.ui.dateEdit_time.dateChanged.connect(self.changeTimeWidget)
        self.ui.timeEdit_globalFirst.timeChanged.connect(self.fixIndividualFirstTimes)
        self.ui.timeEdit_globalLast.timeChanged.connect(self.fixIndividualLastTimes)
        self.ui.pushButton_resettimerange.clicked.connect(self.resetTimeRange)

        # Events (notipage)
        self.ui.pushButton_search.clicked.connect(self.notiSearch)

        # Events (searchpage)
        self.ui.pushButton_extend.clicked.connect(self.extendTime)
        self.ui.pushButton_end.clicked.connect(self.endSearch)
        
    ####### Main flow functions #######
    # Functions handling the flow of the application (loading pages, progressing)
    # Many of these functions use helper functions
    
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
        self.driver.find_element(By.XPATH, '//*[@id="declineButton"]').click()
        
    def dateNext(self):
        # Save info
        self.route = self.ui.comboBox_route.currentText().split('-')
        self.trailer = self.ui.comboBox_trailer.currentText()
        self.n_passengers = self.ui.spinBox_passengers.value()

        self.first_date = self.ui.dateEdit_first.date()
        self.last_date = self.ui.dateEdit_last.date()
        
        delta = self.first_date.daysTo(self.last_date)
        self.n_dates = 1 + delta
        
        # Show waiting screen while program is working
        self.loadPageWait()
        self.ui.stackedWidget.setCurrentIndex(1)
        QTimer.singleShot(10, self.whileWaiting)
        
    
    def whileWaiting(self):
        # Fill in website form
        self.fillFirstPage()
        
        # Load time page
        self.loadPageTime()
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def fillFirstPage(self):
        self.fillRoute()
        self.fillTrailer()
        self.fillPassengers()

        # Next page
        button = self.getElement('div/form/div[3]/div/button')
        self.clickButton(button)
    
    def loadPageWait(self):
        text = '0/' + str(self.n_dates)
        self.ui.label_fetchProg.setText(text)
    
    def loadPageTime(self):
        # Switch to weekly view instead of biweekly
        now_dow = QDate.currentDate().dayOfWeek()
        button = self.getElement('div/form/div/div[3]/div/div/button[' +
                                 str(now_dow) + ']')
        self.clickButton(button)
        
        self.wait_while_loading()

        # Create a TimeWidget for each departure date
        self.setupTimeWidgets()
        
        # Set up date-chooser according to the created TimeWidgets
        self.first_date = self.time_widgets[0].date
        self.last_date = self.time_widgets[-1].date
        delta = self.first_date.daysTo(self.last_date)
        self.n_dates = 1 + delta
        
        self.ui.dateEdit_time.setDate(self.first_date)
        self.ui.dateEdit_time.setMinimumDate(self.first_date)
        self.ui.dateEdit_time.setMaximumDate(self.last_date)

    def timeNext(self):
        # Store the desired range of departure times
        for w in self.time_widgets:
            desired = [False]*len(w.dep_times)
            idx_first = w.comboBox_timefirst.currentIndex()
            idx_last = w.comboBox_timelast.currentIndex()
            for i in range(idx_first, idx_last+1):
                desired[i] = True
            w.desired = desired
            
        self.ui.stackedWidget.setCurrentIndex(3)

    def notiSearch(self):
        mail = self.getMailAddress()
        if mail == None:
            return
        
        self.noti_email = mail
        self.search_freq = 5 * 60000

        self.ui.stackedWidget.setCurrentIndex(4)
        self.start_time = QDateTime.currentDateTime()
        self.end_time =  self.start_time.addSecs(self.var['init_search_hours'] * 3600)
        self.startSearchLoop()
    
    def extendTime(self):
        self.end_time = self.end_time.addSecs(self.var['extend_search_hours'] * 3600)
        self.ui.pushButton_extend.setEnabled(False)
        
        # Update search-end time text
        text = self.ui.label_endTime.text()
        end_time = self.end_time.toString('hh:mm')
        text = re.sub('..:..', end_time, text)
        self.ui.label_endTime.setText(text)
    
    def endSearch(self):
        self.driver.close()
        self.close()
    
    ####### General helper functions #######
    # Helper functions which can be used in many parts of the application

    def rand_sleep(self, sec, u=0.2):
        noise = random.random()*2 - 1
        time.sleep(sec + sec*u*noise)
    
    def wait_while_loading(self, timeout=-1):
        if timeout < 0:
            timeout = self.var['timeout_secs']
            
        self.rand_sleep(0.2)
        WebDriverWait(self.driver, timeout).until(loading_is_done((By.XPATH, '//div[@class="ml-loading-icon"]')))
        
    def wait_for_elem(self, xpath, timeout=-1, wait=0):
        if timeout < 0:
            timeout = self.var['timeout_secs']
            
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="booking"]/' + xpath)))
        self.rand_sleep(wait)

    def getElement(self, xpath, timeout=-1, wait=0):
        if timeout < 0:
            timeout = self.var['timeout_secs']
            
        self.rand_sleep(wait)
        button = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="booking"]/' + xpath)))
        return button

    def getElements(self, xpath, timeout=-1, wait=0):
        if timeout < 0:
            timeout = self.var['timeout_secs']
            
        self.rand_sleep(wait)
        return self.driver.find_elements(By.XPATH, '//*[@id="booking"]/' + xpath)

    def clickButton(self, button, timeout=-1, wait=0):
        if timeout < 0:
            timeout = self.var['timeout_secs']
            
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(button))
        self.rand_sleep(wait)
        button.click()
    
    def weekDiff(self, date_first, date_last):
        # If first comes after last, swap first and last, and multiply by -1
        mult = 1
        if date_first > date_last:
            date_first, date_last = date_last, date_first
            mult = -1
        
        day_diff = date_first.daysTo(date_last)
        first_dow = date_first.dayOfWeek()
        week_diff = int((day_diff + first_dow - 1)/7)
        
        return mult * week_diff
    
    ####### Specific helper functions #######
    # Helper functions that have one specific usage, e.g. filling a specific
    # field or reading the value of a specific element on the website

    def fillRoute(self):
        combobox_xpath = ['div/form/div/div[3]/div[1]/button',
                          'div/form/div/div[3]/div[2]/button']
        options_xpath = ['div/form/div/div[3]/div[1]/div/div/div/div/div/button',
                         'div/form/div/div[3]/div[2]/div/div/div/div/div/button']
        
        for i in range(2):
            combobox = self.getElement(combobox_xpath[i])
            self.clickButton(combobox)
            
            self.rand_sleep(0.5)
            
            # Create a dictionary from options and click the option with matching text
            options = self.getElements(options_xpath[i])
            enum = enumerate(options)
            d = dict((option.text, idx) for idx, option in enum)
            self.clickButton(options[d[self.route[i]]])
    
    def fillTrailer(self):
        if self.ui.comboBox_trailer.currentIndex() > 0:
            button = self.getElement('div/form/div[3]/div/div[2]/div/div[2]/button')
            checkbox = self.getElement('div/form/div[3]/div/div[2]/div/div[2]/button/input')
            
            # Change the status of the checkbox if it's not already correct
            if not checkbox.get_property('checked'):
                self.clickButton(button)
            
            # Select trailer
            buttons = self.getElements(
                'div/form/div[3]/div/div[2]/div/div[3]/div[2]/div/div/button', wait=2)
            self.clickButton(
                buttons[self.ui.comboBox_trailer.currentIndex()-1])
    
    def fillPassengers(self):
        # If trailer-checkbox is checked, the input field is in div[4] instead of div[3]
        checkbox = self.getElement('div/form/div[3]/div/div[2]/div/div[2]/button/input')
        field = None
        if checkbox.get_property('checked'):
            field = self.getElement(
                'div/form/div[3]/div/div[2]/div/div[4]/div/div/div/input')
        else:
            field = self.getElement(
                'div/form/div[3]/div/div[2]/div/div[3]/div/div/div/input')
            
        field.send_keys(Keys.BACKSPACE)
        field.send_keys(self.n_passengers)
    
    def setupTimeWidgets(self):
        self.time_widgets = []
        self.rand_sleep(1)
        
        # Create a TimeWidget for each date
        for i in range(self.n_dates):
            # Update counter on waiting page
            text = str(i+1) + '/' + str(self.n_dates)
            self.ui.label_fetchProg.setText(text)
            self.ui.label_fetchProg.repaint()
            
            date = self.first_date.addDays(i)
            deps_available, deps_time = self.getAvailableDepartures(date)
            if len(deps_time) > 0:
                self.time_widgets.append(TimeWidget(date, deps_time, deps_available))
        
        # Create a stackedwidget page for each date (after removing the existing stackedwidget)
        self.ui.time_layout.removeWidget(self.ui.time_layout.itemAt(2).widget())
        self.ui.stackedWidget_time = QStackedWidget()
        self.ui.time_layout.insertWidget(2, self.ui.stackedWidget_time)
        for w in self.time_widgets:
            self.ui.stackedWidget_time.addWidget(w)
            
    def getAvailableDepartures(self, date, second_attempt=False):
        self.goToDate(date)
        date_buttons = self.getElements('div/form/div')[2:]
        
        # Check if returned list contains departures or just the "no departures" element
        if len(date_buttons) == 1:
            if date_buttons[0].get_attribute('class') == 'departure-and-ticket__code':
                # Try one more time to make sure that we aren't getting trolled
                if second_attempt:
                    return [], []
                else:
                    print('Lemme try again')
                    return self.getAvailableDepartures(date, True)
        
        deps_available = self.getAvailable(date_buttons)
        deps_time = self.getDepTimes(date_buttons)
        
        return deps_available, deps_time
    
    def goToDate(self, date):
        week_diff = self.weekDiff(self.getSelectedDate(), date)
        button = None
        
        if week_diff > 0:
            button = self.getElement('div/form/div[1]/div[3]/button')
        elif week_diff < 0:
            week_diff = -week_diff
            button = self.getElement('div/form/div[1]/div[1]/button')
        
        # Go to correct week
        for i in range(week_diff):
            self.clickButton(button)
        
        # Go to correct date
        dow = date.dayOfWeek()
        button = self.getElement('div/form/div[1]/div[2]/div/div/button[' + 
                                 str(dow) + ']')
        self.clickButton(button)
        
        # Wait for departures to load
        self.wait_while_loading()
        
        
    def getSelectedDate(self):
        buttons = self.getElements('div/form/div[1]/div[2]/div/div/button')
        dow = 1
        for button in buttons:
            if '-selected' in button.get_attribute('class'):
                break
            dow += 1
        
        date_string = buttons[dow-1].text.split('\n')
        
        if date_string[1] == 'I dag':
            return QDate.currentDate()
        
        d = int(date_string[0])
        m = self.months[date_string[1]]
        y = QDate.currentDate().year()
        
        return QDate(y, m, d)
    
    def getDepTimes(self, deps):
        deps_times = []
        for dep in deps:
            deps_times.append(dep.find_element(
                By.XPATH, 'div/button/button/div[1]/div[1]/div[2]').text)
        return deps_times
    
    def getAvailable(self, deps):
        # Last piece of text is 'Udsolgt' if tickets are unavailable
        return [dep.text.split()[-1] != 'Udsolgt' for dep in deps]
    
    def getMailAddress(self):
        mail = self.ui.lineEdit_mail.text()

        # Mail must contain one '@' between two strings
        mail_split = mail.split('@')
        if len(mail_split) != 2:
            return
        if not all(len(s) > 0 for s in mail_split):
            return
        
        # Mail must contain one or more '.' after the '@'.
        # There must be a string before and after each '.'
        mail_split_split = mail_split[1].split('.')
        if len(mail_split_split) < 2:
            return
        if not all(len(s) > 0 for s in mail_split_split):
            return
        
        return mail

    def fixLastDate(self):
        if self.ui.dateEdit_first.date() > self.ui.dateEdit_last.date():
            self.ui.dateEdit_last.setDate(self.ui.dateEdit_first.date())

    def fixFirstDate(self):
        if self.ui.dateEdit_first.date() > self.ui.dateEdit_last.date():
            self.ui.dateEdit_first.setDate(self.ui.dateEdit_last.date())
    
    def fixIndividualFirstTimes(self):
        first_time = self.ui.timeEdit_globalFirst.time().toString('hh:mm')
        for w in self.time_widgets:
            for i in range(w.comboBox_timefirst.count()):
                if w.comboBox_timefirst.itemText(i) >= first_time:
                    w.comboBox_timefirst.setCurrentIndex(i)
                    break
    
    def fixIndividualLastTimes(self):
        last_time = self.ui.timeEdit_globalLast.time().toString('hh:mm')
        for w in self.time_widgets:
            for i in range(w.comboBox_timelast.count()-1, 0, -1):
                if w.comboBox_timelast.itemText(i) <= last_time:
                    w.comboBox_timelast.setCurrentIndex(i)
                    break
    
    def resetTimeRange(self):
        self.ui.timeEdit_globalFirst.setTime(QTime(0,0))
        self.ui.timeEdit_globalLast.setTime(QTime(23,59))
        self.fixIndividualFirstTimes()
        self.fixIndividualLastTimes()
        
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
            
    ####### Search loop functions #######
    # Functions used specifically for the search loop
        
    def startSearchLoop(self):
        # Display search-end time text
        text = self.ui.label_endTime.text()
        end_time = self.end_time.toString('hh:mm')
        text = re.sub('..:..', end_time, text)
        self.ui.label_endTime.setText(text)
        
        # Mail currently available departures
        if self.ui.checkBox_current.isChecked():
            subject = 'Ledige billetter'
            text = 'Ledige afgange:'
            
            for w in self.time_widgets:
                date_string = '\n' + w.date.toString('dd/MM:')
                dep_string = ''
                for i in range(len(w.dep_times)):
                    if w.available[i] & w.desired[i]:
                        dep_string += '\n' + w.dep_times[i]
                
                if dep_string != '':
                    text += date_string + dep_string + '\n'
                
            self.sendNotification(subject, text)
        
        
        QTimer.singleShot(self.search_freq, self.searchLoop)

    def searchLoop(self):
        time_until_end = QDateTime.currentDateTime().secsTo(self.end_time)
        if time_until_end <= 0:
            subject = 'Soegning er afsluttet fordi tiden er loebet ud'
            text = 'Fordi soegetiden er ikke blevet forlaenget, er tiden loebet ud, og programmet er blevet stoppet'
            self.sendNotification(subject, text)
            self.endSearch()
        else:
            try:
                if time_until_end < self.var['extend_search_hours'] * 3600:
                    self.ui.pushButton_extend.setEnabled(True)
                
                # Result string which will be sent to receiver email
                result = 'Nye ledige afgange:'
                
                # Check availability for each date
                has_any_new_available = False
                
                for w in self.time_widgets:
                    date_string = '\n' + w.date.toString('dd/MM:')
                    dep_string, is_available = \
                        self.getNewAvailableString(w)
                    
                    if dep_string != '':
                        has_any_new_available = True
                        result += date_string + dep_string + '\n'
                    
                    # If all departures on the first date are passed, remove that date
                    if (len(is_available) == 0) & (w.date == self.first_date):
                        self.first_date = self.first_date.addDays(1)
                        self.time_widgets = self.time_widgets[1:]
                        print('Removed the date ' + w.date.toString('dd/MM:'))
                        
                        if self.first_date > self.last_date:
                            subject = 'Soegning er afsluttet fordi alle relevante afgange er passeret'
                            text = 'Alle valgte afgange er passeret, så soegningen er stoppet'
                            self.sendNotification(subject, text)
                            self.endSearch()
                        
                    # Remove passed departures and update availability
                    elif len(w.available) > len(is_available):
                        print('changed ' + w.date.toString('dd/MM:') + ' from')
                        print(w.dep_times)
                        print(w.available)
                        len_diff = len(w.available) - len(is_available)
                        w.dep_times = w.dep_times[len_diff:]
                        print('to')
                        print(w.dep_times)
                        print(is_available)
                    w.available = is_available
                        
                
                if has_any_new_available:
                    subject = 'Nye ledige billeter'
                    self.sendNotification(subject, result)
                
                self.exception_streak = 0
                
                QTimer.singleShot(self.search_freq, self.searchLoop)
                
            except Exception:
                traceback.print_exc()
                self.exception_streak += 1
                
                if self.exception_streak > 5:
                    subject = 'Soegning er afsluttet pga. fejl'
                    text = 'Programmet har obhobet for mange fejl og er derfor blevet stoppet'
                    self.sendNotification(subject, text)
                    self.endSearch()
                    
                # Restart search
                self.driver.get('https://www.bornholmslinjen.dk/booking')
                self.rand_sleep(1)
                
                self.fillFirstPage()
                
                # select today's date
                now_dow = QDate.currentDate().dayOfWeek()
                button = self.getElement('div/form/div/div[3]/div/div/button[' +
                                         str(now_dow) + ']')
                self.clickButton(button)
                self.wait_while_loading()
                
                # Continue the search
                self.searchLoop()
    
    def getNewAvailableString(self, time_widget):
        date = time_widget.date
        deps_available, deps_time = self.getAvailableDepartures(date)
        
        # Trim the previous list of available (in case departures have passed)
        n_deps = len(deps_available)
        is_available = deps_available
        was_available = time_widget.available[-n_deps:]
        
        # Check if new departures have become available
        text = ''
        for i in range(len(deps_time)):
            if not was_available[i] and is_available[i]:
                if time_widget.desired[i]:
                    text += '\n' + deps_time[i]
        
        return text, is_available
    
    def sendNotification(self, subject, text):
        message = 'Subject: ' + subject + '\n\n' + text

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.var['smtp_server'],
                              self.var['port'], context=context) as server:
            server.login(self.var['sender'], self.var['password'])
            server.sendmail(self.var['sender'], self.noti_email, message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = KombardoPinger()
    widget.show()
    app.exec_()
