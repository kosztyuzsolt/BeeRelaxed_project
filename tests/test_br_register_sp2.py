from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os
from BeeRelaxed.utils import generate_unique_email, get_verification_code

from BeeRelaxed.page_models.br_register_page_model import BeerelaxedRegisterPage
from BeeRelaxed.generate_browser import get_configured_chrome_driver

URL = 'http://localhost:4200/'

class TestBeerelaxedRegister:

    def setup_method(self):
        self.browser = get_configured_chrome_driver()
        self.page = BeerelaxedRegisterPage(URL, self.browser)
        self.page.open()

    def teardown_method(self):
        self.page.close_browser()

    def test_register_happy_path(self):
        unique_email = generate_unique_email()
        file_path = os.path.join(os.path.dirname(__file__), "..", "test_data", "BeePic_Bee.png")
        file_path = os.path.abspath(file_path)
        self.page.fill_form_register("Dani", "Dongo", "12345678", unique_email, "Teszt123", "1111", "City", "Address", file_path, "Beekeeper")

        verification_code = get_verification_code(unique_email)
        self.page.verify_registration(unique_email, verification_code)

        assert self.page.text_verification().text == "Verification Successful"
        self.page.close_form().click()