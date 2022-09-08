from selenium.webdriver import Firefox
import pytest
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.fixture()
def setPath():
    global driver
    path = "C:\\Users\\zeyne\\Documents\\drivers\\geckodriver"
    driver =Firefox(executable_path=path)
    yield
    driver.quit()

def test_dropdown_handle(setPath):
    driver.get("https://en-gb.facebook.com/reg/")
    driver.maximize_window()
    sleep(5)
    selectDay = Select(driver.find_element(By.ID, 'day'))
    selectDay.select_by_index(10)
    sleep(5)
    selectMonth = Select(driver.find_element(By.ID, 'month'))
    selectMonth.select_by_index(10)
    sleep(5)
    selectYear = Select(driver.find_element(By.ID, 'year'))
    selectYear.select_by_index(10)
    #selectDay.select_by_value("20")
    #selectDay.select_by_visible_text('20')
    sleep(5)