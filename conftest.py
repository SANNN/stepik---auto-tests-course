import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options

# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="None",
                     help="Choose language: ru, en and others")

# To run example: $pytest -s -v --browser_name=firefox test_parser.py
# To run example: $pytest -s -v --browser_name=chrome test_parser.py
# To run example: $pytest -v --tb=line --reruns 1 --browser_name=chrome --language=en test_rerun.py
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
    	options = Options()
    	options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    	print("\nstart chrome browser for test..")
    	browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
    	fp = webdriver.FirefoxProfile()
    	fp.set_preference("intl.accept_languages", user_language)
    	print("\nstart firefox browser for test..")
    	binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    	browser = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()