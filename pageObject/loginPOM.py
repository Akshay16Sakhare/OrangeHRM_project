import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

class LoginPage():

    text_usename_name = (By.NAME, "username")
    text_password_name = (By.NAME, "password")
    click_login_btn = (By.XPATH, "//button[@type='submit']")
    click_menu_btn = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    click_logout_btn = (By.XPATH, "//a[normalize-space()='Logout']")
    click_Admin_btn = (By.XPATH, "//li[1]//a[1]//span[1]")
    userInput_text_box = (By.XPATH, "//input[@class='oxd-input oxd-input--focus']")
    click_Search_btn = (By.XPATH, "//button[normalize-space()='Search']")

    def __init__(self, driver):
        self.driver =driver
        self.wait = WebDriverWait(self.driver,5)

    def Enter_username(self,username):
        element = self.wait.until(EC.visibility_of_element_located(self.text_usename_name))
        element.send_keys(username)
        # self.driver.find_element(*self.text_usename_name).send_keys(username)

    def Enter_password(self,password):
        self.driver.find_element(*self.text_password_name).send_keys(password)

    def Click_login_btn(self):
        self.driver.find_element(*self.click_login_btn).click()

    def Login_status(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.click_menu_btn))
            self.driver.find_element(*self.click_menu_btn)
            return True
        except NoSuchElementException:
            return False
            pass

    def Click_menu_btn(self):
        element = self.wait.until(EC.visibility_of_element_located(self.click_menu_btn))
        self.driver.find_element(*self.click_menu_btn).click()

    def Click_logout_btn(self):
        self.driver.find_element(*self.click_logout_btn).click()

    def Click_Admin_btn(self):
        self.driver.find_element(*self.click_Admin_btn).click()

    def Enter_userInput_text(self,userInput):
        ele = self.driver.find_element(*self.userInput_text_box)
        ele.clear()
        ele.send_keys(userInput)

    def Click_Search_btn(self):
        self.driver.find_element(*self.click_Search_btn).click()
