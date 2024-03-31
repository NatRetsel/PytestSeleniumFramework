from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import List

class ConfirmPage():
    text_box = (By.ID, "country")
    link_text = (By.LINK_TEXT, "India")
    check_box = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_button = (By.CSS_SELECTOR, "input[type='submit']")
    success_text = (By.CLASS_NAME, "alert")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def findTextBox(self) -> WebElement:
        return self.driver.find_element(*ConfirmPage.text_box)
    
    def findLinkText(self) -> WebElement:
        return self.driver.find_element(*ConfirmPage.link_text)
    
    def findCheckBox(self) -> WebElement:
        return self.driver.find_element(*ConfirmPage.check_box)
    
    def findPurchaseButton(self) -> WebElement:
        return self.driver.find_element(*ConfirmPage.purchase_button)
    
    def findSuccessText(self) -> str:
        return self.driver.find_element(*ConfirmPage.success_text).text