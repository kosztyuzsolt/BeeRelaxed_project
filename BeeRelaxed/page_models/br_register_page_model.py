from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import uuid
from BeeRelaxed.general_page import GeneralPage

class BeerelaxedRegisterPage(GeneralPage):
    def __init__(self, URL, browser):
        super().__init__(URL, browser)
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def button_register(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Register"]')))

    def input_firstname(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'firstName')))

    def input_lastname(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'lastName')))

    def input_phone(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'phoneNumber')))

    def input_email(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'email')))

    def generate_unique_email(prefix="testuser", domain="dongo.hu"):
        return f"{prefix}_{uuid.uuid4().hex[:8]}@{domain}"

    def input_password(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'password')))

    def input_zipcode(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'zipcode')))

    def input_city(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'city')))

    def input_address(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'address')))

    def input_role(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'role')))

    def select_role(self, role):
        Select(self.input_role()).select_by_visible_text(role)

    def input_file_upload(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, 'featureImageUrl')))

    def upload_file(self, file_path):
        self.input_file_upload().send_keys(file_path)

    def button_submit(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Submit"]')))

    def click_submit(self):
        button = self.button_submit()
        ActionChains(self.browser).move_to_element(button).click().perform()

    def button_login(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Login"]')))

    def input_verification_code(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'verificationCode')))

    def enter_verification_code(self, code):
        self.input_verification_code().send_keys(str(code))

    def input_verification_email(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'emailV')))

    def button_verify_registration(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Verify Registration "]')))

    def verify_registration(self, email, code):
        self.input_verification_email().send_keys(email)
        self.enter_verification_code(code)
        self.button_verify_registration().click()

    def text_verification(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, '//small[text()=" Verification Successful "]')))

    def close_form(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Close "]')))


# - HELPER METHODS -------------------------------------------------------

    def fill_form_register(self, firstname, lastname, phone, email, password, zipcode, city, address, file_path, role):
        self.button_register().click()
        self.input_firstname().send_keys(firstname)
        self.input_lastname().send_keys(lastname)
        self.input_phone().send_keys(phone)
        self.input_email().send_keys(email)
        self.input_password().send_keys(password)
        self.input_zipcode().send_keys(zipcode)
        self.input_city().send_keys(city)
        self.input_address().send_keys(address)
        self.upload_file(file_path)
        self.select_role(role)
        self.click_submit()


