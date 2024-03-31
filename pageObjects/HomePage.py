from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from pageObjects.CheckoutPage import CheckoutPage
from selenium.webdriver.remote.webelement import WebElement

class HomePage():
    # store in terms of (locator, value) as a class variable
    # we can use regex for partial search
    # not recommended but good to know
    # equivalent for XPATH //a[contains(@href,'shop')]
    shop=(By.CSS_SELECTOR,"a[href*='shop']")
    email=(By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    name = (By.CSS_SELECTOR, "input[name='name']")
    studentRadio = (By.CSS_SELECTOR, "#inlineRadio1")
    textBox = (By.XPATH, "(//input[@type='text'])[3]")
    submitButton = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")
    
    def __init__(self, driver:WebDriver ) -> None:
        self.driver = driver

    def shopItems(self) -> CheckoutPage:
        self.driver.find_element(*HomePage.shop).click() #unpacks the tuple as first and second parameters
        return CheckoutPage(self.driver)
    
    def getEmail(self) -> WebElement:
        return self.driver.find_element(*HomePage.email)
    
    def getPassword(self) -> WebElement:
        return self.driver.find_element(*HomePage.password)
    
    def getCheckbox(self) -> WebElement:
        return self.driver.find_element(*HomePage.checkbox)
    
    def getGender(self) -> WebElement:
        return self.driver.find_element(*HomePage.gender)
    
    def getName(self) -> WebElement:
        return self.driver.find_element(*HomePage.name)
    
    def getStudentRadio(self) -> WebElement:
        return self.driver.find_element(*HomePage.studentRadio)
    
    def getTextBox(self) -> WebElement:
        return self.driver.find_element(*HomePage.textBox)
    
    def getSubmitButton(self) -> WebElement:
        return self.driver.find_element(*HomePage.submitButton)
    
    def getAlertText(self) -> str:
        return self.driver.find_element(*HomePage.alert).text
