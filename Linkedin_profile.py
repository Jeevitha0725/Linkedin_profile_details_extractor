from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import json
from selenium.webdriver.support.wait import WebDriverWait
import os

driver = webdriver.Chrome()
def login():
    driver.get("https://www.linkedin.com/login")
    time.sleep(1)

    eml = driver.find_element(by=By.ID, value="username")
    eml.send_keys("s.jeevitha234@gmail.com")
    passwd = driver.find_element(by=By.ID, value="password")
    passwd.send_keys("JeeviSagiraju007")
    loginbutton = driver.find_element(
        by=By.XPATH, value="//*[@id='organic-div']/form/div[3]/button")
    loginbutton.click()
    time.sleep(3)


def search():
    link = open(r'C:\Users\sjeev\Documents\Python\pythonProject\LInkedin_user_links\links.txt')
    line = link.readlines()
    with open(r"C:\Users\sjeev\Documents\Python\pythonProject\LInkedin_user_links\links.txt") as fp:
        n = sum(1 for line in fp)  # for counting no. of lines

    data = ""
    list1 = ""

    for i in range(n):
        search_t = driver.get(line[i]+"overlay/contact-info/")
        time.sleep(3)

        source = BeautifulSoup(driver.page_source, features="html.parser")

        mail = "no result"
        website = "no result"
        phno = "no result"
        for record in source.findAll("div", {"class": "artdeco-modal__header ember-view"}):
            person = record.text.replace(",", '.')
            person = person.replace("\n", '')

        for record in source.findAll("a", {"class": "pv-contact-info__contact-link link-without-visited-state t-14"}):

            mail = record.text.replace(" ", '')
            mail = mail.replace("\n", '')

            data = person + ',' + mail

        for record in source.findAll("div", {"class": "pv-profile-section__section-info section-info"}):
            for record1 in record("a", {"class": "pv-contact-info__contact-link link-without-visited-state"}):

                    website = record1.text.replace(" ", '')
                    website = website.replace("\n", '')
            for record1 in record("li", {"class": "pv-contact-info__ci-container t-14"}):

                phno = record1.text.replace(" ", '')
                phno = phno.replace("\n", '')

            data = data + ',' + website
            data = data + "," + phno

        list1 = list1 + '\n' + data
    print(list1)



    header = "Name,Email ID,Website,Phone No."
    file = open(os.path.expanduser("linkedin data.csv"), "wb")
    file.write(bytes(header, encoding="ascii", errors="ignore"))
    file.write(bytes(list1, encoding="ascii", errors="ignore"))


login()
search()
