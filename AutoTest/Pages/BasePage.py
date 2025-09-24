from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pathlib import Path


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Получаем абсолютный путь к HTML-файлу
        html_path = Path(__file__).parent.parent / "Lab3AutoReg" / "contact.html"
        self.base_url = f"file://{html_path.absolute()}"

    def find_element(self, locator, time=10):
        """Поиск одного элемента с явным ожиданием"""
        try:
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator),
                message=f"Can't find element by locator {locator}"
            )
        except TimeoutException:
            return print(TimeoutException)

    def go_to_site(self):
        """Переход на базовый URL страницы"""
        return self.driver.get(self.base_url)