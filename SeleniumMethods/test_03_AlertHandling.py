from selenium.webdriver import Chrome
import pytest
from selenium.webdriver.common.by import By
from time import sleep

#global level
path = "C:\\Users\\zeyne\\Documents\\drivers\\chromedriver"
driver = Chrome(executable_path=path)
@pytest.mark.Chrome
def test_alert_handling():
    driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
    driver.maximize_window()
    driver.find_element(By.NAME,'proceed').click()
    sleep(5)
    alert_handling()
    driver.close()


def alert_handling():
    alert = driver.switch_to.alert
    assert alert.text == "Please enter a valid user name"
    alert.accept()
