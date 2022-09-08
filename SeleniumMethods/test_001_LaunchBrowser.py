import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from time import sleep
@pytest.mark.Firefox
def test_chrome_browser():
    path = "C:\\Users\\zeyne\\Documents\\drivers\\chromedriver"
    driver = Chrome(executable_path=path)
    driver.get("https://app.hubspot.com/login")
    sleep(5)
    driver.maximize_window()
    assert driver.title == "HubSpot Login"
    print("url is : "+driver.current_url)
    driver.quit()
@pytest.mark.FF
def test_firefox_browser():
    path = "C:\\Users\\zeyne\\Documents\\drivers\\geckodriver"
    driver = Firefox(executable_path=path)
    driver.get("https://app.hubspot.com/login")
    sleep(5)
    driver.maximize_window()
    assert driver.title == "HubSpot Login"
    print("url: ", driver.current_url)
    driver.close()
