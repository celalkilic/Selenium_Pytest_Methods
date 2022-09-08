from selenium.webdriver import Firefox
import pytest
from time import sleep

@pytest.mark.Firefox
def test_screenshot():
    path = "C:\\Users\\zeyne\\Documents\\drivers\\geckodriver"
    driver = Firefox(executable_path=path)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    sleep(5)
    directory = "C:\\Users\\zeyne\\Desktop\\celal\\screenshot.png"
    driver.get_screenshot_as_file(directory)
    driver.close()