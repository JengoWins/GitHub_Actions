import pytest
from Pages.conftest import browser
from Pages.ContactPage import ContactPage

# Данные для позитивного теста
valid_name = "Иван Иванов"
valid_email = "test@example.com"
valid_phone = "+79991234567"  # Необязательное поле
valid_message = "Это тестовое сообщение для проверки контактной формы."
valid_pass = "Aaaaa12!"


def test_successful_form_submission(browser):  # Фикстура 'browser' задается в conftest.py
    # 1. Инициализация и переход на страницу
    contact_page = ContactPage(browser)
    contact_page.go_to_site()

    # 2. Действие: Заполнение и отправка формы
    contact_page.fill_form_and_submit(
        name=valid_name,
        password=valid_pass,
        email=valid_email,
        message=valid_message,
        phone=valid_phone
    )

    # 3. Проверка (Утверждение): Сообщение об успехе отображается
    assert contact_page.is_success_message_displayed(), "Сообщение об успешной отправке не появилось"
