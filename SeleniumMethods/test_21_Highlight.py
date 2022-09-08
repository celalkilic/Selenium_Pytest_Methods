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

def test_highlighted_element(setPath):
   driver.maximize_window()
   driver.get("https://www.facebook.com")
   element = driver.find_element(By.ID, "email")
   element.send_keys("ilhan")

   driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                         "background: yellow; border: 3px solid red;")
   sleep(2)