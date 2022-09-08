from selenium.webdriver import Firefox, ActionChains
import pytest
from time import sleep

from selenium.webdriver.common.by import By


@pytest.fixture()
def setPath():
    global driver
    path = "C:\\Users\\zeyne\\Documents\\drivers\\geckodriver"
    driver = Firefox(executable_path=path)
    yield
    driver.quit()

def test_right_click(setPath):
    driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
    sleep(3)
    driver.maximize_window()

    action = ActionChains(driver)
    action.context_click(driver.find_element(By.XPATH, "//span[@class = 'context-menu-one btn btn-neutral']")).perform()
    sleep(5)
    driver.find_element(By.XPATH, "// ul[ @class = 'context-menu-list context-menu-root'] / li[3]").click()
    sleep(5)
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()

