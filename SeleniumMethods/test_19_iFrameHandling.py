from selenium.webdriver import Chrome
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture()
def setPath():
    global driver
    path = "C:\\Users\\zeyne\\Documents\\drivers\\chromedriver"
    driver = Chrome(executable_path=path)
    yield
    driver.quit()

def test_iFrame(setPath):
    driver.maximize_window()
    driver.get("http://londonfreelance.org/courses/frames/index.html")

    driver.switch_to.frame(driver.find_element(By.NAME, "main"))
    header = driver.find_element(By.CSS_SELECTOR, "body > h2")
    print("\n", header.text )

    driver.switch_to.default_content()
    print(driver.title)