import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    """
    Фикстура для инициализации и закрытия браузера.
    Scope='function' означает, что браузер создается и закрывается для каждого теста.
    """
    # Настройка опций Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Максимизировать окно
    chrome_options.add_argument("--disable-notifications")  # Отключить уведомления
    chrome_options.add_argument("--disable-extensions")  # Отключить расширения
    #chrome_options.add_argument("--headless")  # Раскомментировать для безголового режима

    # Инициализация драйвера
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Передача драйвера тесту
    yield driver

    # Закрытие браузера после завершения теста
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    return "../Lab3AutoReg/contact.html"  # Замените на реальный URL


# Хуки для настройки поведения pytest
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выбор браузера: chrome, firefox, edge"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск в headless режиме"
    )
