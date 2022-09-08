import pytest

# to execute windows we need to write this command on the console
# pytest PytestSamples/test_Demo_selectorDiselect.py -m windows -v
@pytest.mark.windows
def test_windows_1():
    assert True
@pytest.mark.windows
def test_windows_2():
    assert True

# to execute mac we need to write this command on the console
# pytest PytestSamples/test_Demo_selectorDiselect.py -m mac -v
@pytest.mark.mac
def test_mac_1():
    assert True
@pytest.mark.mac
def test_mac_2():
    assert True

# you want to fail your test you need to write .xfail extension
@pytest.mark.xfail
def test_fail_1():
    assert False
@pytest.mark.xfail
def test_fail_2():
    assert False