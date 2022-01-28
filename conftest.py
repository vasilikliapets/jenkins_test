import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--remote-debugin-port=9222")
    options.add_argument("--screen-size=1200x800")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Remote(desired_capabilities=options.to_capabilities())

    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
