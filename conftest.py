import pytest
from selene import browser

@pytest.fixture(scope="function")
def browser_size():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()

@pytest.fixture(scope="function")
def browser_size_v2():
    browser.config.window_height = 540
    browser.config.window_width = 320
    yield
    browser.quit()



