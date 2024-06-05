import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def init_driver(request):
    service_chrome = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_chrome)
    driver.maximize_window()
    driver.get("https://formy-project.herokuapp.com/")
    driver.set_page_load_timeout(30)
    request.cls.driver = driver

    yield
    driver.quit()


