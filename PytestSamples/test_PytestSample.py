from selenium.webdriver import Chrome
import pytest
from selenium.webdriver.common.by import By

class TestSample():
    @pytest.fixture()
    def setPath(self):
        global driver
        path = "C:\\Users\\zeyne\\Documents\\drivers\\chromedriver"
        driver = Chrome(executable_path=path)
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print()
        print("test completed")

    def test_login_orangeHRM(self, setPath):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, 'username').send_keys("Admin")
        driver.find_element(By.NAME, 'password').send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        title  = driver.title
        assert title == "OrangeHRM"

