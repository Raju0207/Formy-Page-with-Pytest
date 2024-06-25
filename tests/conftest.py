import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture()
def init_driver(request):
    option = ChromeOptions()
    option.add_argument("--headless")
    option.add_argument('--window-size=1920,1080')
    service_chrome = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_chrome, options=option)
    driver.maximize_window()
    driver.get("https://formy-project.herokuapp.com/")
    driver.set_page_load_timeout(30)
    request.cls.driver = driver
    print("Test case started.............")

    yield
    print("Test completed..............")
    driver.quit()
