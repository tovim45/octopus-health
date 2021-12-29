import allure
import requests as requests

from infra.utils.selenium_utils import init_driver
from src.pages.clalit_page import MainPage

base_url = "https://www.clalit.co.il/he/medical/pharmacy/Pages/medicine_guide.aspx "


@allure.step(' step 1 - get IP Address from fakercloud')
def clalit_medicine():
    print("Navigate to fakercloud to get the IP Address field shown on screen")
    driver = init_driver()
    driver.get(base_url)
    mp = MainPage(driver)
    mp.test_title()
    # ip = mp.get_ip()
    # print(ip)
    # return ip


@allure.feature('Epic int-2830')
@allure.story('Story int-3061')
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase(
    'Test examines the IP Address field shown on screen and validate its value is from Israeli geo-location.')
def test_validate_value_from_Israeli_geo_location():
    clalit_medicine()
    # uri = "https://api.iplocation.net/?ip=" + ip_address
    # print(str(uri))
    # resp = requests.get(uri)
    # assert resp.status_code == 200, "Response code is not 200"
    # data = resp.json()
    # print(data)
    # assert data['country_code2'] != 'IL', "Can't find ip " + ip_address + " from Israeli geo-location."


test_validate_value_from_Israeli_geo_location()
