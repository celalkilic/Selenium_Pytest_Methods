from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import pytest
from time import sleep

@pytest.mark.Chrome
def test_alert_ahndling():
    path = "C:\\Users\\zeyne\\Documents\\drivers\\chromedriver"
    driver = Chrome(executable_path=path)
    driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
    driver.maximize_window()
    driver.find_element(By.NAME, 'proceed').click()
    sleep(4)
    alert = driver.switch_to.alert
    assert alert.text == "Please enter a valid user name"
    alert.accept()
    driver.close()