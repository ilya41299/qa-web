from pydantic import SecretStr
from selenium.webdriver.support import expected_conditions as EC

from page_components.component import Component, timeout_wrapper


class Input(Component):
    @property
    def type_of(self) -> str:
        return "input"

    @timeout_wrapper("Ввод текста в {type_of} '{locator_name}'")
    def fill(self, text: str | SecretStr):
        self._get_element().send_keys(
            text.get_secret_value() if isinstance(text, SecretStr) else text
        )

    @timeout_wrapper(
        "Очистка поля и ввод текста в {type_of} '{locator_name}'",
    )
    def clear_and_fill(self, text: str | SecretStr):
        input_field = self._get_element()
        input_field.click()
        input_field.clear()
        input_field.send_keys(
            text.get_secret_value() if isinstance(text, SecretStr) else text
        )

    def fill_and_validate(self, text: str | SecretStr):
        self.clear_and_fill(text)
        self.should_have_text(
            text=text.get_secret_value() if isinstance(text, SecretStr) else text
        )

    @property
    def text(self) -> str:
        return self._get_element().get_attribute("value")

    @timeout_wrapper(
        "Проверить что {type_of} '{locator_name}' имеет текст '{text}'",
    )
    def should_have_text(self, *, text: str = "") -> None:
        self._page.wait.until(
            EC.text_to_be_present_in_element_value(self.locator["locator"], text)
        )
