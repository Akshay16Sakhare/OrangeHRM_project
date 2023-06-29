import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from pageObject.loginPOM import LoginPage
from utilities.readConfigfiles import Read_values
from utilities.Logger import LogGen

class Test_login:

    get_username = Read_values.getUser()
    get_password = Read_values.getPasswrd()
    logs = LogGen.loggen()

    def test_URL_001(self, setup):
        self.logs.debug("debug")
        self.logs.info("info")
        self.logs.warning("warning")
        self.logs.error("error")
        self.logs.critical("critical")

        self.driver = setup
        self.logs.info("Open Browser")
        time.sleep(5)
        self.logs.info("checking page title")
        if self.driver.title == 'OrangeHRM':
            self.logs.info("test_URL_001 is passed")
            # time.sleep(5)
            self.driver.save_screenshot(r"C:\Users\Admin\PycharmProjects\Project_orangeHRM\screenshots\test_URL_001_pass.png")
            assert True
        else:
            self.logs.info("test_URL_001 is failed")
            self.driver.save_screenshot(r"C:\Users\Admin\PycharmProjects\Project_orangeHRM\screenshots\test_URL_001_fail.png")
            assert False
        self.driver.close()
        self.logs.info("test_URL_001 is completed")

    def test_Login_002(self, setup):
        self.logs.info("going to url")
        self.driver = setup
        self.login_attribute = LoginPage(self.driver)
        self.logs.info("username entered" + self.get_username)
        self.login_attribute.Enter_username(self.get_username)
        self.logs.info("password entered" + self.get_password)
        self.login_attribute.Enter_password(self.get_password)
        self.logs.info("click Login Button")
        self.login_attribute.Click_login_btn()

        if self.login_attribute.Login_status() == True:
            self.logs.info("test_Login_002 Login passed")
            self.driver.save_screenshot(r"C:\Users\Admin\PycharmProjects\Project_orangeHRM\screenshots\test_Login_002_pass.png")
            self.logs.info("click Menu Button")
            self.login_attribute.Click_menu_btn()
            self.logs.info("click Logout Button")
            self.login_attribute.Click_logout_btn()
            assert True
        else:
            self.logs.info("test_Login_002 Login failed")
            self.driver.save_screenshot(r"C:\Users\Admin\PycharmProjects\Project_orangeHRM\screenshots\test_Login_002_fail.png")
            assert False
        self.driver.close()
        self.logs.info("test_Login_002 is completed")

    # def test_Search_user(self,setup):
    #     self.driver = setup
    #     time.sleep(2)
    #     self.login_attribute = LoginPage(self.driver)
    #     self.login_attribute.Enter_username('Admin')
    #     self.login_attribute.Enter_password('admin123')
    #     self.login_attribute.Click_login_btn()
    #     time.sleep(2)
    #     self.login_attribute.Click_Admin_btn()
    #     time.sleep(5)
    #     self.login_attribute.Enter_userInput_text('Akshay')
    #     time.sleep(5)
    #     self.login_attribute.Click_Search_btn()
    #     self.login_attribute.Click_menu_btn()
    #     self.login_attribute.Click_logout_btn()
