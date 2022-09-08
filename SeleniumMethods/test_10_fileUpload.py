from selenium.webdriver import Firefox, ActionChains
import pytest
from time import sleep
from selenium.webdriver.common.by import By

@pytest.fixture()
def setPath():
    global driver
    path = "C:\\Users\\zeyne\\Documents\\drivers\\geckodriver"
    driver =Firefox(executable_path=path)
    yield
    driver.quit()
def test_file_upload(setPath):
    driver.maximize_window()
    driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")
    driver.find_element(By.NAME).send_keys("C:\\Users\\zeyne\\Desktop\\celal\\demo.txt")