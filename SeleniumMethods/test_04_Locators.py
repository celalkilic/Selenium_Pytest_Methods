from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

path = "C:\\Users\\zeyne\\Documents\\drivers\\geckodriver"
driver = webdriver.Firefox(executable_path=path)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
#by name
element = driver.find_element(By.NAME, 'username')
element.send_keys('Admin')
element = driver.find_element(By.NAME, 'password')
element.send_keys('admin123')
element = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
element.click()
driver.close()


