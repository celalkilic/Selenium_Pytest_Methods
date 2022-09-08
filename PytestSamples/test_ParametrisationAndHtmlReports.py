import pytest

def sum(a,b):
    return a+b
@pytest.mark.parametrize("input, input2, output",
                         [
                            (2,2,4),
                            (3,3,6),
                            (5,5,10)
                         ])
def test_sum_1(input, input2, output):
    result = sum(input,input2)
    assert result == output

# 1. pytest html reports
# to take this kind of report we need to install html report by writing this command on the terminal
# pip install html-reports
# then to take report to our system we need to write this on the terminal a report will create in our package
# pytest PytestSamples/ --html=PytestSamples/report1.html
# to see report1.html right click, browsers, Chrome browser click.

# 2.pytest html report without css(assets folder)
# to do that we need to write this code to terminal
# pytest PytestSamples/ --html=PytestSamples/reports/report1.html --self-contained-html
