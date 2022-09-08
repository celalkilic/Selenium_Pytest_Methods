from selenium.webdriver import Firefox
import pytest


@pytest.fixture()
def setPath():
    global driver
    path = "C:\\Users\\zeyne\\Documents\\drivers\\geckodriver"
    driver =Firefox(executable_path=path)
    yield
    driver.quit()
def test_assertion(setPath):
    driver.maximize_window()
    driver.get("https://app.hubspot.com/login")
    actualTitle = driver.title
    assert actualTitle == "HubSpot Login"
    print("actual title is ",actualTitle)