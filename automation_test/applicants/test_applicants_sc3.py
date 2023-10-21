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

class Test_Applicants_Scenario_3_Detail(Basic_Test):
    @pytest.mark.parametrize('driver_init', ['chrome'], indirect=True)
    def test_open_url(self):
        self.driver.get(BASE_URL + 'admin/applicant')

        time.sleep(2)
        phone_number = self.driver.find_element(By.XPATH, '//*[@id="datatables"]/tbody/tr[1]/td[5]').text
        self.driver.find_element(By.XPATH, '//*[@id="datatables"]/tbody/tr[1]/td[10]/div/a[1]').click()

        detail_phone_number = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[2]/div[1]/table/tbody/tr[7]/td').text
        assert_that(detail_phone_number).contains(phone_number)

        time.sleep(3)