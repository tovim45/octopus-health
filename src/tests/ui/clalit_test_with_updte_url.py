import codecs
import json

import allure
import pandas

from infra.utils.selenium_utils import init_driver
from src.pages.clalit_page import MainPage

base_url = "https://www.clalit.co.il/he/medical/pharmacy/Pages/medicine_guide.aspx?freeText=text_to_find&sender=SubmitClick"
csv_file = "src/test_data/medications.csv"
output_result_file = "reports/result_not_found_medicines.json"


def read_csv_data_file():
    return pandas.read_csv(csv_file, index_col=0)


def write_output_file(data):
    with codecs.open(output_result_file, 'a', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(". ", " = "))
        f.write("\n")
        f.close()


@allure.feature('Epic int-2830')
@allure.story('Story int-3061')
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase('Test that that writes to a file the names of medications that do not have an info page in the '
                 'Clalit medications portal with update url.')
def test_validate_value_of_medicine_from_clalit_portal():
    print("Navigate to Clalit web portal")
    driver = init_driver()
    mp = MainPage(driver)
    medicines = read_csv_data_file()
    for medicine in medicines.index:
        driver.get(base_url.replace("text_to_find", medicine))
        mp.enter_medicine_to_search(medicine)
        mp.click_search_submit()
        result = mp.get_medicine_search_result()
        if result == '0':
            result_data = {medicine: int(result)}
            print(result_data)
            write_output_file(medicine)


test_validate_value_of_medicine_from_clalit_portal()
