import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeSerivce
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture(scope="class")
def setup(request,browser,url):
        # lauch webbrowser and type the url
        if browser == "chrome":
            driver = webdriver.Chrome(service=ChromeSerivce(ChromeDriverManager().install()))
        elif browser == 'ff':
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == 'edge':
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(6)
        driver.get(url)
        request.cls.driver = driver
        yield
        driver.close()

def pytest_addoption(parser):
        parser.addoption("--browser")
        parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
        return request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def url(request):
        return request.config.getoption("--url")

