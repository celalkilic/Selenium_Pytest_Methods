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
def test_drog_drop(setPath):
    driver.maximize_window()
    driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
    drag = driver.find_element(By.ID, 'draggable')
    sleep(5)
    drop = driver.find_element(By.ID,'droppable')
    sleep(5)
    action = ActionChains(driver)
    action.drag_and_drop(drag, drop).perform()
