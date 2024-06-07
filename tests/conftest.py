import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


def pytest_addoption(parser):
    # (key), default_value, help (optional text)
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )



@pytest.fixture(scope="class")
# We can have request as an instance of the fixture.
# Then we can link our fixture instance to our class that requires driver
def setup(request):
    # retrieve command line value store in a variable
    browser_name = request.config.getoption("browser_name")

    # Probably should use switch case
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver: WebDriver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        driver:WebDriver = webdriver.Firefox()
    elif browser_name == "edge":
        driver:WebDriver = webdriver.Edge()

    driver.implicitly_wait(5) #will wait max 5s for element to show up / load. Think of it as global timeout
    driver.get("https://rahulshettyacademy.com/angularpractice") # Uses get method on the URL
    
    # initialized local driver is assigned as a class object / class variable called driver
    # So whichever class uses this fixture will have access to the driver under the variable name driver
    # Why we do this? We may try to include a return statement returning the driver but statements below
    # it. i.e. yield onwards will never be reached.
    request.cls.driver=driver 

    yield
    driver.close()
