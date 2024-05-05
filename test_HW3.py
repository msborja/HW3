
from selene import browser, be, have

def test_bing_success(browser_size):
    browser.open('https://www.bing.com/')
    (browser.element('[name="q"]').should(be.blank).type('Python 3.12 download').press_enter())
    browser.element('[class="b_algo"]').should(have.text('Python.org'))

def test_duckduckgo_success(browser_size):
    browser.open('https://duckduckgo.com')
    (browser.element('[class="searchbox_input__bEGm3"]').should(be.blank).type('Python 3.12 download').press_enter())
    browser.element('[class="EKtkFWMYpwzMKOYr0GYm LQVY1Jpkk8nyJ6HBWKAk"]').should(have.text('Python.org'))

def test_googlee_unsuccess(browser_size):
    browser.open('https://google.com')
    (browser.element('[name="q"]').should(be.blank).type(
        'selene mod version 3.0.0 download torrent plz 123456789010').press_enter())
    browser.element('[class="card-section"]').should(have.text(
        'selene mod version 3.0.0 download torrent plz 123456789010'))