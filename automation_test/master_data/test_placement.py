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

class Test_Placement_Search(Basic_Test):
    @pytest.mark.parametrize('driver_init', ['chrome'], indirect=True)
    def test_open_url(self):
        self.driver.get(BASE_URL + 'admin/master/placement')
        search_param = 'waru'

        time.sleep(2)
        search_text_field = self.driver.find_element(By.NAME, 'search')
        search_text_field.send_keys(search_param)
        self.driver.find_element(By.ID, 'dt-btn-search').click()

        time.sleep(3)
        length_table = len(self.driver.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr'))
        for i in range(length_table):
          datatable_name = self.driver.find_element(By.XPATH, f'//*[@id="datatables"]/tbody/tr[{i + 1}]/td[2]').text
          assert_that(datatable_name.lower()).contains(search_param.lower())
