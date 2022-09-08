from selenium.webdriver import Chrome, ActionChains
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
def test_mouse_hover(setPath):
    driver.get("https://www.verizonwireless.com/moxie/moxieFront.jsp")
    sleep(5)
    driver.maximize_window()
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.CSS_SELECTOR, "label[for='EBbusiness']")).perform()
    sleep(5)
    phone = driver.find_element(By.CSS_SELECTOR, "a[href='http://www.verizon.com/business/']")
    phone.click()