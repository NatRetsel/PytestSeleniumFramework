from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time
from typing import List
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage

"""
Best practices
1.) Browser invocation code should not be in test methods/cases.
    i.e. we don't want 
        def test_e2e():
            driver: WebDriver = webdriver.Chrome()
            driver.implicitly_wait()
            driver.get(url)
    - We want it in a separate file -> i.e. fixture so it can be grabbed by the test cases
    - Reason: if not, we have to include the same lines in every test case

2.) Setting up a base test class
    - Supposed every test classes will be requiring the setup fixture
    - We do not want to keep repeating the same decorators above every test classes
    - Setting up a baseclass and decorating the setup fixture allows all other classes
    to have access to the fixture by inheriting the baseclass
    - pros - easy to read

3.) Selecting browser at run time through command line
    - Previously hardcoded browser type in fixture
    - How can we modify setup fixture to run the different browsers based on what was sent in command line?
        - specify how to pass command line options to pytest through hook in key value pairs

4.) Page object design
    - notice in our e2e test we are retrieving items by locating them within the test method
    - POD stores contents necessary to fetch webElements for each page in one class
    - Pros: readability

5.) Removing page object creation statements in test
    - find integration interaction point -> know which webpage appears, thus the corresponding page object
    - create the object at the interaction point and return it

6.) Keep generalised functions in the baseclass
    - e.g. explicit wait
    - select from dropdown with given text

7.) Remove hardcoded data in Page Data classes to allow test to run with multiple datasets from external sources
    - using dictionary
    - from excel file
"""

# @pytest.mark.usefixtures("setup") - commented out because inherited from BaseClass
class TestOne(BaseClass):
    def test_e2e(self):
        logger = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        logger.info("Getting all items")
        # Supposed we want Blackberry but we do not know which position it is in
        # Choose a selector that encompass all the products / relevant products and iterate the list for our
        # desired product
        
        products: List[WebElement] = checkoutPage.getProductsTitles()

        for product in products:
            productName:str = CheckoutPage.getProductTitle(product)
            if productName == "Blackberry":
                logger.info(productName)
                CheckoutPage.findAddToCartButton(product).click()

        checkoutPage.findCheckoutButton().click()
        

        confirmPage = checkoutPage.findCheckoutButtonConfirm()
        logger.info("Populating autosuggestive text with 'ind'")
        confirmPage.findTextBox().send_keys("ind")

        self.verifyLinkPresence("India")
        
        confirmPage.findLinkText().click()
        confirmPage.findCheckBox().click()
        confirmPage.findPurchaseButton().click()

        successText = confirmPage.findSuccessText()
        logger.info("Text received from alert: " +successText)
        assert "Success! Thank you!" in successText
        