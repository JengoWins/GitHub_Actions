from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ContactPage(BasePage):
    # ЛОКАТОРЫ (селекторы элементов)
    NAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    EMAIL_INPUT = (By.ID, "email")
    PHONE_INPUT = (By.ID, "phone")
    MESSAGE_TEXTAREA = (By.ID, "textarea")
    SUCCESS_ALERT = (By.ID, "complete")
    ERROR_MESSAGES = (By.CLASS_NAME, "-error")

    # МЕТОДЫ ВЗАИМОДЕЙСТВИЯ
    def enter_name(self, name):
        self.find_element(self.NAME_INPUT).send_keys(name)

    def enter_email(self, email):
        self.find_element(self.EMAIL_INPUT).send_keys(email)

    def enter_phone(self, phone):
        self.find_element(self.PHONE_INPUT).send_keys(phone)

    def enter_message(self, message):
        self.find_element(self.MESSAGE_TEXTAREA).send_keys(message)

    def enter_password(self, password):
        self.find_element(self.PASSWORD_INPUT).send_keys(password)

    def click_submit(self):
        self.find_element(self.SUBMIT_BUTTON).click()

    # МЕТОДЫ-ПРОВЕРКИ
    def is_success_message_displayed(self, expected_text="Форма успешно отправлена!"):
        """Проверяет, отобразилось ли сообщение об успехе с ожидаемым текстом"""
        element = self.find_element(self.SUCCESS_ALERT)
        if element:
            return expected_text in element.text
        return False

    def get_error_messages(self):
        """Возвращает список текстов всех ошибок валидации на странице"""
        error_elements = self.driver.find_elements(*self.ERROR_MESSAGES)
        return [error.text for error in error_elements if error.is_displayed()]

    # УНИВЕРСАЛЬНЫЙ МЕТОД ДЛЯ ПОЗИТИВНОГО ТЕСТА
    def fill_form_and_submit(self, name, email, message, password, phone=None, ):
        """Заполняет все поля формы и отправляет ее."""
        self.enter_name(name)
        self.enter_email(email)
        self.enter_message(message)
        self.enter_password(password)
        if phone:
            self.enter_phone(phone)
        self.click_submit()
