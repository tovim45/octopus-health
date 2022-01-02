from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.ui import WebDriverWait as W


class MainPage:
    title = 'מדריך התרופות | שירותי בריאות כללית'
    wait_time_out = 20
    medicine_id = '//input[@id="txtServiceSearch"]'
    search_submit = '//button[@id="searchSubmit"]'
    medicine_locator_name = '//*[@id="medicine_search_results_list"]//child::*//child::*[1]'
    x_search = '//input[@id="txtServiceSearch"]'

    def __init__(self, drv):
        self.drv = drv
        self.wait_variable = W(self.drv, self.wait_time_out)

    def test_title(self):
        print(self.title + " page title is the OK and equal to: " + self.drv.title)
        assert self.title in self.drv.title

    def enter_medicine_to_search(self, search_medicine):
        self.wait_variable.until(E.presence_of_element_located((By.XPATH, self.medicine_id))).clear()
        self.wait_variable.until(E.presence_of_element_located((By.XPATH, self.medicine_id))).send_keys(search_medicine)

    def click_search_submit(self):
        self.wait_variable.until(E.element_to_be_clickable((By.XPATH, self.search_submit))).click()

    def get_medicine_search_result(self):
        return self.wait_variable.until(E.element_to_be_clickable((By.XPATH, self.medicine_locator_name))).text

    def click_x_search(self):
        self.wait_variable.until(E.element_to_be_clickable((By.XPATH, self.x_search))).click()

    @staticmethod
    def scroll_to_top(driver):
        driver.execute_script("scroll(0, 0);")
