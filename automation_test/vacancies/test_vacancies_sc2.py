import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from setting.endpoint import BASE_URL
from selenium.webdriver.support.ui import Select
from assertpy import assert_that


def select_option(self, element, val):
  self.driver.find_element(By.ID, element[0]).click()
  time.sleep(3)
  length = len(self.driver.find_element(By.ID, element[1]).find_elements(By.TAG_NAME, 'li'))
  time.sleep(3)
  for i in range(length):
    item = self.driver.find_element(By.XPATH, f'//*[@id="{element[1]}"]/li[{i + 1}]')
    if item.text == val:
      return item

@pytest.mark.usefixtures("driver_init")
class Basic_Test:
    pass

class Test_Vacancies_Scenario_2(Basic_Test):
    @pytest.mark.parametrize('driver_init', ['chrome'], indirect=True)
    def test_open_url(self):
        self.driver.get(BASE_URL + 'admin/vacancy')
        job_level_selector = ["select2-job_level_id-container", "select2-job_level_id-results"]
        job_placement_selector = ["select2-placement-container", "select2-placement-results"]
        job_education_selector = ["select2-education_id-container", "select2-education_id-results"]
        job_contract_selector = ["select2-contract_id-container", "select2-contract_id-results"]
        job_status_selector = ["select2-availability-container", "select2-availability-results"]

        job_level = select_option(self, job_level_selector, "Senior")
        job_level.click()

        job_placement = select_option(self, job_placement_selector, "On Site Waru")
        job_placement.click()

        job_education = select_option(self, job_education_selector, "D4/S1")
        job_education.click()

        job_contract = select_option(self, job_contract_selector, "Part Time")
        job_contract.click()

        job_status = select_option(self, job_status_selector, "Available")
        job_status.click()

        start_date = self.driver.find_element(By.ID, "starts_end_date")
        start_date.send_keys("20-08-2023")

        end_date = self.driver.find_element(By.ID, "ends_end_date")
        end_date.send_keys("12-10-2023")

        self.driver.find_element(By.ID, "dt-btn-filter").click()

        time.sleep(2)
        no_data_shown = self.driver.find_element(By.ID, "datatables_info").text
        assert_that(no_data_shown).is_equal_to("No data to be shown! (filtered from 4 total data)")

        time.sleep(3)
