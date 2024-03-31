import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param

    def test_formSubmission(self, getData):

        logger = self.getLogger()
        self.driver.refresh()
        homePage:HomePage = HomePage(self.driver)
        #Locators: ID, Xpath, CSSSelector, Classname, name, linkText
        # Right-click inspect and identify the html tags pertaining to the field of interest 
        logger.info("Filling email - " +getData["email"])
        homePage.getEmail().send_keys(getData["email"])
        logger.info("Filling password - " +getData["password"])
        homePage.getPassword().send_keys(getData["password"])
        homePage.getCheckbox().click()


        #Static dropdown
        # <select>
        logger.info("Selecting Gender - " +getData["gender"])
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        
        

        #Xpath, CSSSelector
        # Useful to locate elements where the developers did not give it attributes supported as Selenium as locators
        # For every element in the page, we can construct the Xpath and CSS

        # CSSSelector
        # tagname[attribute='value'] -> //input[type='submit'], #id, .className
        logger.info("Filling name - " +getData["name"])
        homePage.getName().send_keys(getData["name"])
        homePage.getStudentRadio().click()

        # Xpath
        # //tagname[@attribute='value'] -> //input[@type='submit']
        # Inspect the element of interest and select the attribute
        # if multiple Xpath are present, we can bracket the value and index however multiple-way binding can happen
        logger.info("Filling text box - " +getData["text"])
        homePage.getTextBox().send_keys(getData["text"])
        homePage.getTextBox().clear()
        homePage.getSubmitButton().click()
        msg:str = homePage.getAlertText()
        print(msg)
        assert "Success" in msg
        
        