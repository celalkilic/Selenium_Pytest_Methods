from selenium.webdriver import Chrome
import pytest
from time import sleep

@pytest.mark.Chrome
def test_navigate_browser():
    path = "C:\\Users\\zeyne\\Documents\\drivers\\chromedriver"
    driver = Chrome(executable_path=path)
    driver.get("https://www.ebay.com")
    driver.maximize_window()
    sleep(2)
    driver.get("https://www.amazon.com")
    driver.maximize_window()
    sleep(2)
    driver.back()
    driver.maximize_window()
    sleep(2)
    driver.forward()
    driver.maximize_window()
    sleep(2)
    driver.back()
    driver.maximize_window()
    sleep(2)
    driver.refresh()
    driver.maximize_window()
    driver.close()