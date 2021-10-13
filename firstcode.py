from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://simplygore-trials72.orangehrmlive.com/")
driver.find_element(By.ID, "txtUsername").send_keys('Admin')
driver.find_element(By.ID, "txtPassword").send_keys('96WUBg@Oju')
driver.find_element(By.ID, "btnLogin").click()

assert driver.title == 'Dashboard', 'Title does not matched'

print('yes title matched')