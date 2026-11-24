from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_configured_chrome_driver():
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument('--guest')
    options.add_argument('window-position=0,-900')
    browser = webdriver.Chrome(options=options)
    return browser

def get_configured_firefox_driver():
    browser = webdriver.Firefox()
    return browser


if __name__ == '__main__':
    firefox_driver = get_configured_firefox_driver()
    firefox_driver.get("http://www.google.com")
    print(__name__)


