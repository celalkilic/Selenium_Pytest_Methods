import pytest
import sys
# to skip test we need to define @pytest.mark.skip(reason='none included in this build')
# to see skipping reason on the console we need to write this command on the terminal
# pytest PytestSamples/test_Demo_skip.py -v -rxs
@pytest.mark.skip(reason='none included in this build')
def test_demo_1():
    assert True
def test_demo_2():
    assert True
# to execute only one test case we need to write this command on the console
# pytest PytestSamples/test_Demo_skip.py -v -rxs -k test_demo_3

"""skipif
If you wish to skip something conditionally then you can use skipif instead. Here is an 
example of marking a test function to be skipped when run on an interpreter earlier than Python3.10:
import sys
@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")"""
@pytest.mark.skipif(sys.version_info > (3, 10), reason="requires python3.10 or higher")
def test_demo_3():
    assert True
def test_demo_4():
    assert True
