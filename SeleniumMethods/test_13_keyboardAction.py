from selenium.webdriver import Chrome
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def setPath():
    global driver
    path = "C:\\Users\\zeyne\\Documents\\drivers\\chromedriver"
    driver = Chrome(executable_path=path)
    yield
    driver.quit()

def test_google_search(setPath):
    driver.maximize_window()
    driver.get("https://www.booking.com/")
    driver.find_element(By.ID, "ss").send_keys("Manchester")
    sleep(2)
    driver.find_element(By.ID, "ss").send_keys(Keys.ARROW_DOWN)
    sleep(2)
    driver.find_element(By.ID,"ss").send_keys(Keys.ENTER)

def test_copy_paste(setPath):
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    driver.find_element(By.ID, "email").send_keys("python")
    sleep(2)
    driver.find_element(By.ID, "email").send_keys(Keys.CONTROL, "a")
    sleep(2)
    driver.find_element(By.ID, "email").send_keys(Keys.CONTROL, "c")
    sleep(2)
    driver.find_element(By.ID, "pass").send_keys(Keys.CONTROL, "v")
    sleep(2)