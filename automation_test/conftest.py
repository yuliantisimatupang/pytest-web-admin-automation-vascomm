import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from setting.endpoint import URL_LOGIN


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()

    web_driver.get(URL_LOGIN)
    web_driver.maximize_window()

    email_text_field = web_driver.find_element(By.ID, "email")
    password_text_field = web_driver.find_element(By.ID, "password")
    email_text_field.send_keys("qatestvascomm@gmail.com")
    password_text_field.send_keys("juPJegXS")
    password_text_field.submit()

    request.cls.driver = web_driver
    time.sleep(2)
    yield
    web_driver.close()

@pytest.fixture(scope='function', autouse=True)
def hook(request):
  print('\nbefore suite f')
  yield
  print('\nafter suite f')

@pytest.fixture(scope='session', autouse=True)
def suite(request):
  print('\nbefore suite')
  yield
  print('\nafter suite')