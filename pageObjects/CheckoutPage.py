from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from pageObjects.ConfirmPage import ConfirmPage

class CheckoutPage():
    products = (By.XPATH,"//div[@class='card h-100']")
    product = (By.XPATH,"div[@class='card-body']/h4/a")
    addToCartbutton = (By.XPATH, "div/button")
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutButtonConfirm = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
    
    def getProductsTitles(self) -> List[WebElement]:
        return self.driver.find_elements(*CheckoutPage.products)

    @staticmethod
    def getProductTitle(item: WebElement) -> List[str]:
        return item.find_element(*CheckoutPage.product).text
    
    @staticmethod
    def findAddToCartButton(item: WebElement) -> WebElement:
        return item.find_element(*CheckoutPage.addToCartbutton)
    
    def findCheckoutButton(self) -> WebElement:
        return self.driver.find_element(*CheckoutPage.checkoutButton)
    
    def findCheckoutButtonConfirm(self) -> ConfirmPage:
        self.driver.find_element(*CheckoutPage.checkoutButtonConfirm).click()
        return ConfirmPage(self.driver)