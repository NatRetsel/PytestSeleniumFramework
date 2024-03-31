import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import logging
import inspect

@pytest.mark.usefixtures("setup")
class BaseClass():
    
    def verifyLinkPresence(self, text_to_verify: str):
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,text_to_verify)))

    def selectOptionByText(self, locator:WebElement, text:str):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text) 
    
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName) #catches filename

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.INFO)
        return logger