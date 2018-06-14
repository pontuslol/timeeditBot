#!/usr/bin/python2.4
# -*- coding: utf-8 -*-
import datetime

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

#typ att man behöver göra en sak som är true bara ifall titeln alltså assert är Timeedit annars så kör den om den
#ifall sidan är överbelastad.
#om inte adressen kommer fram alltså om sidan
# är nere så görs en trycatch och gör hela koden till  en funtkion som kommer
#att köras igen tills driver.get(URL) är sann och även att assert är rätt vilket säkerställer
#även att man har kommit fram denna måste täcka all kod på sidan mer eller mindre.

#Vilken sida drivern ska ta oss till
driver.get("https://se.timeedit.net/web/liu/db1/wr_stud/")

r = requests.get("https://se.timeedit.net/web/liu/db1/wr_stud/")

print r.text

#Se till att det står TimeEdit i titeln, för att säkerställa att navigationen har gått rätt till
assert "TimeEdit" in driver.title

#Klickar logga in när drivern tagit oss till timeedits-bokningssystem
loginTimeEdit = driver.find_element_by_xpath('/html/body/div[2]/div/table/tbody/tr/td/div/form/div/a[1]')
loginTimeEdit.click()

#Fyller i användarnamn på LISAM LIU
#loginLisamUsername = driver.find_element_by_id('userNameInput')
loginLisamUsername = driver.find_element_by_xpath('//*[@id="userNameInput"]')
loginLisamUsername.send_keys("ponte582")

#Fyller i lösenord på LISAM LIU
#loginLisamPassword = driver.find_element_by_id('passwordInput')
loginLisamPassword = driver.find_element_by_xpath('//*[@id="passwordInput"]')
loginLisamPassword.send_keys("Sadelmakare1")

#Loggar in på LISAM LIU
#loginLisamClick = driver.find_element_by_id('submitButton')
loginLisamClick = driver.find_element_by_xpath('//*[@id="submitButton"]')
loginLisamClick.click()

#Väljer studentbokning på LIUS hemsida
chooseStudentBokning = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div/div[1]/a[1]/div/span[1]/span')
chooseStudentBokning.click()

#Behöver en funktion som adderar en dag på den aktuella dagen, och den dagen ska sedan väljas
#de två sista teckena i det nya datumet ska sedan jämföras med Tidsschemat nedanför och sedan välja
#just den spalten. Detta för att sedan trycka på 10-14 i just den dagen och sen klicka okej.

tomorrow_date = (datetime.datetime.now() + datetime.timedelta(days=1))  #datetime.datetime
tomorrow_year = str(tomorrow_date.year)      #int
tomorrow_month = tomorrow_date.month        #int
tomorrow_day = tomorrow_date.day            #int
if tomorrow_month < 10:
    tomorrow_month = "0"+str(tomorrow_month)
else:
    tomorrow_month = str(tomorrow_month)

if tomorrow_day < 10:
        tomorrow_day = "0"+str(tomorrow_day)
else:
    tomorrow_day = str(tomorrow_day)

date_button = driver.find_element_by_xpath('//*[@id="leftresdate"]')
date_button.clear()
date_button.click()
date_button.send_keys(str(tomorrow_year) + "-" + str(tomorrow_month) + "-" + str(tomorrow_day))

chooseOnlyAvailable = driver.find_element_by_xpath('//*[@id="timeHourSpec3"]')
chooseOnlyAvailable.click()
 
#Tar fram tiden 10
chooseStart = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/table/tbody/tr/td[3]/div/select[1]/option[4]')
chooseStart.click()
 
#Tar fram tiden 14
chooseEnd = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/table/tbody/tr/td[4]/div/select[1]/option[8]')
chooseEnd.click()

#Trycker på RUM AG21
chooseAG21 = driver.find_element_by_xpath('//*[@id="objectselectionresult"]/table/tbody/tr[2]/td[2]')
chooseAG21.click()

#Klicka på klockan 10 i schemat
#chooseTimeStartRoom = driver.find_element_by_xpath('')
#chooseTimeStartRoom.click()

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Härifrån kan du läsa Jens. Jag fattar inte om jag har gjort rätt. 
#Men jag försökte att skapa en likadan funktion som dig där uppe fast utan 0 innan om det är mindre än 10 för det är inte nödvändigt enligt mig.
#den konverterar sedan till string och lägger ihop dom, hoppas att det blev rätt.

#tror dessa tre kommande rader ska fungera...
chooseNextTomorrow_date = (datetime.datetime.now() + datetime.timedelta(days=1))

chooseNextDay = chooseNextTomorrow_date.day
chooseNextMonth = chooseNextTomorrow_date.month

chooseNextDay = str(chooseNextDay) #Konvertera int to String
chooseNextMonth = str(chooseNextMonth) #Konvertera int to string

NextDayInTable = "%s/%s"%(chooseNextDay,chooseNextMonth)
print NextDayInTable

#   3. Gör en funktion som jämför den nya stringen compare med alla strings på hemsidan för att matcha rätt DIV (alltså rätt dag)