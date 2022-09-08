from selenium.webdriver import Chrome
import pytest
from time import sleep

from selenium.webdriver.common.by import By


@pytest.fixture()
def setPath():
    global driver
    path = "C:\\Users\\zeyne\\Documents\\drivers\\chromedriver"
    driver = Chrome(executable_path=path)
    yield
    driver.quit()

def test_radio_button(setPath):
    driver.maximize_window()
    driver.get("file:\\C:\\Users\\zeyne\\PycharmProjects\\Selenium_Pytest_Methods\\files\\index.html")
    sleep(3)
    element = driver.find_element(By.XPATH, "//input[@value='Mango']")
    print("\nBEFORE: ", element.is_selected())
    element.click()
    sleep(2)
    print("\nAFTER: ", element.is_selected())