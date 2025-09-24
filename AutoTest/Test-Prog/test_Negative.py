from selenium.webdriver.support import expected_conditions as EC
from Pages.conftest import browser
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from Pages.ContactPage import ContactPage

# Данные для негативного теста
valid_name = "Иван Иванов"
valid_email = "test@example.com"
valid_phone = "+79991234567"  # Необязательное поле
valid_message = "Это тестовое сообщение для проверки контактной формы."
valid_pass = "234sf"


def test_negative_submission(browser):
    # 1. Инициализация и переход на страницу
    contact_page = ContactPage(browser)
    contact_page.go_to_site()

    # 2. Действие: Заполнение и отправка формы
    contact_page.fill_form_and_submit(
        name=valid_name,
        email=valid_email,
        message=valid_message,
        phone=valid_phone,
        password=valid_pass
    )
    errors = contact_page.get_error_messages()

    assert not contact_page.is_success_message_displayed(), "Неожиданно появилось сообщение об успехе при ошибке валидации"
    if len(errors) == 0:
        raise AssertionError("Ожидались сообщения об ошибках, но их нет") # Проверяем, что хотя бы в одном сообщении об ошибке есть ключевое слово
