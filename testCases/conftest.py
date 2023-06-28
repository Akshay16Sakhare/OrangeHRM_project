import pytest
from selenium import webdriver
from selenium.webdriver.common import by


@pytest.fixture
def setup():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("headless")
    driver = webdriver.Chrome() #options=chrome_options
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.maximize_window()
    return driver
