from selenium import webdriver
import time

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
signButtonXpath = "/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div[2]/button"
emailFieldXpath = "/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div[1]/input"

browser.get("https://www.geeksforgeeks.org/python/how-to-install-selenium-in-python/")
time.sleep(1.5)
signInButton = browser.find_element(By.XPATH, signButtonXpath)
print("Clicking on Sign In button")
signInButton.click()
time.sleep(2)
emailField = browser.find_element(By.XPATH, emailFieldXpath)
emailField.send_keys("ahmadisloggingin")

time.sleep(5)
print("Done")
