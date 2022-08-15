from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = "C:/SeleniumDriver/chromedriver.exe"
url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
driver = webdriver.Chrome(path)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(url)
print(driver.title)
driver.find_element(By.CLASS_NAME, "btn-lg").click()
driver.find_element(By.NAME, "userSelect").click()
driver.close()

file_one = open("firstfile.txt", "w")
print(file_one.write("my first line to the file"))
file_one.close()

file_read = open("firstfile.txt", "r")
print(file_read.readline())
