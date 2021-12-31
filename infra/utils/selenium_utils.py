import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


def init_driver():
    """
    Init selenium Web driver for chrome only
    :return: driver
    """

    exec_path = r"driver/chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path=exec_path, chrome_options=chrome_options)
    driver.maximize_window()
    driver.delete_all_cookies()
    return driver


def get_screenshot(driver, name):
    """
    Add screenshot to Allure report
    :param driver:
    :param name:
    """
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
