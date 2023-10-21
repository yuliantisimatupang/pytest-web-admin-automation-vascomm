import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from setting.endpoint import BASE_URL
from selenium.webdriver.support.ui import Select
from assertpy import assert_that


@pytest.mark.usefixtures("driver_init")
class Basic_Test:
    pass

class Test_Vacancies_Scenario_3(Basic_Test):
    @pytest.mark.parametrize('driver_init', ['chrome'], indirect=True)
    def test_open_url(self):
        self.driver.get(BASE_URL + 'admin/vacancy')

        time.sleep(2)
        vacancy_name = self.driver.find_element(By.XPATH, '//*[@id="datatables"]/tbody/tr[1]/td[3]').text
        self.driver.find_element(By.XPATH, '//*[@id="datatables"]/tbody/tr[1]/td[9]/div/a[1]').click()

        detail_vacancy_name = self.driver.find_element(By.TAG_NAME, 'h4').text
        assert_that(detail_vacancy_name).contains(vacancy_name)
