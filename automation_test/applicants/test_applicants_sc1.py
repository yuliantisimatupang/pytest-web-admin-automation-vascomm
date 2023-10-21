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

class Test_Applicants_Scenario_1(Basic_Test):
    @pytest.mark.parametrize('driver_init', ['chrome'], indirect=True)
    def test_open_url(self):
        self.driver.get(BASE_URL + 'admin/applicant')
        job_vacancies = Select(self.driver.find_element(By.NAME, "job"))
        job_vacancies.select_by_visible_text("Freelancer UI/UX")

        job_vacancies = Select(self.driver.find_element(By.NAME, "placement"))
        job_vacancies.select_by_visible_text("All Placement")

        job_vacancies = Select(self.driver.find_element(By.NAME, "status"))
        job_vacancies.select_by_visible_text("Applied")

        start_date = self.driver.find_element(By.ID, "starts_apply")
        start_date.send_keys("01-07-2023")

        end_date = self.driver.find_element(By.ID, "ends_apply")
        end_date.send_keys("11-11-2023")

        self.driver.find_element(By.ID, "dt-btn-filter").click()

        time.sleep(2)
        no_data_shown = self.driver.find_element(By.ID, "datatables_info").text
        assert_that(no_data_shown).is_not_equal_to("No data to be shown! (filtered from 4 total data)")

        time.sleep(3)
