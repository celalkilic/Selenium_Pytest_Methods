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
def test_isOptions(setPath):
    driver.get("https://app.hubspot.com/login")
    sleep(5)
    driver.maximize_window()
    print("\ndisplayed ?", driver.find_element(By.CSS_SELECTOR, "i18n-string[data-key='login.signupLink.cta']").is_displayed())
    print("\nenabled ?", driver.find_element(By.CSS_SELECTOR, "i18n-string[data-key='login.signupLink.cta']").is_enabled())
    print("\nselected ?", driver.find_element(By.CSS_SELECTOR, "i18n-string[data-key='login.signupLink.cta']").is_selected())