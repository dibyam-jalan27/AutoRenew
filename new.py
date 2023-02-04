import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])


def startbot(username, password, url):
    global driver
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe", chrome_options=chrome_options)

    driver.get(url)
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("id", "submitButton").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Items Checked out").click()
    time.sleep(1)
    driver.find_element("id", "renewLabel").click()
    driver.quit()