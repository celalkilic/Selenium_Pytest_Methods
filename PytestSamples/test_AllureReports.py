import pytest

# allure reports
# documentation
# https://docs.qameta.io/allure-report/#_pytest
# create a directory named allure_reports then right click on allure_reports copy absolute path then past after this command#
# pytest PytestSamples/ --alluredir=C:\Users\zeyne\PycharmProjects\Selenium_Pytest_Methods\PytestSamples\allure_reports
# then paste this code on terminal
# to take report of allure write this command on the terminal
# allure serve
# then copy allure_reports file absolute xpath after this command
# allure serve C:\Users\zeyne\PycharmProjects\Selenium_Pytest_Methods\PytestSamples\allure_reports
# then a bworser will come up with allure reports
@pytest.mark.windows
def test_windows_1():
    assert True
@pytest.mark.windows
def test_windows_2():
    assert True
@pytest.mark.mac
def test_mac_1():
    assert True
@pytest.mark.mac
def test_mac_2():
    assert True
@pytest.mark.xfail
def test_fail_1():
    assert False
@pytest.mark.xfail
def test_fail_2():
    assert False

