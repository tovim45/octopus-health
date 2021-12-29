# wait for loader
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as W


class MainPage:
    title = 'Faker Cloud - get faked!'
    wait_time_out = 20

    get_ip_address = '//*[@data-example="IP Address"]'

    def __init__(self, drv):
        self.drv = drv
        self.wait_variable = W(self.drv, self.wait_time_out)

    def test_title(self):
        print(self.title + " page title is the OK and equal to: " + self.drv.title)
        assert self.title in self.drv.title

    def get_ip(self):
        ip = self.drv.find_element_by_xpath('//*[@data-example="IP Address"]').get_attribute("value")
        print(ip)
        return ip

    def wait_for_loader(self, driver):
        WebDriverWait(driver, 20).until(EC.cli(
            (By.XPATH, self.all_apps_names)))
