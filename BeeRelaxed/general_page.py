import time

class GeneralPage:
    def __init__(self, URL, browser):
        self.URL = URL
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)

    def get_current_url(self):
        return self.browser.current_url

    def get_current_title(self) -> str:
        return self.browser.title

    def close_browser(self):
        self.browser.close()

    def quit(self):
        self.browser.quit()

    def save_screenshot(self):
        self.browser.save_screenshot(f"screenshot_{time.time}.png")

