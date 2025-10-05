from .base_page import BasePage
from .locators import FormFieldsPageLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


DRINK_MAP = {
    "water": FormFieldsPageLocators.FAVORITE_DRINK_WATER_CHECKBOX,
    "milk": FormFieldsPageLocators.FAVORITE_DRINK_MILK_CHECKBOX,
    "coffee": FormFieldsPageLocators.FAVORITE_DRINK_COFFEE_CHECKBOX,
    "wine": FormFieldsPageLocators.FAVORITE_DRINK_WINE_CHECKBOX,
    "ctrl-alt-delight": FormFieldsPageLocators.FAVORITE_DRINK_CTRL_ALT_DELIGHT_CHECKBOX,
}

COLOR_MAP = {
    "red": FormFieldsPageLocators.FAVORITE_COLOR_RED_RADIO_BUTTON,
    "blue": FormFieldsPageLocators.FAVORITE_COLOR_BLUE_RADIO_BUTTON,
    "yellow": FormFieldsPageLocators.FAVORITE_COLOR_YELLOW_RADIO_BUTTON,
    "green": FormFieldsPageLocators.FAVORITE_COLOR_GREEN_RADIO_BUTTON,
    "#FFC0CB": FormFieldsPageLocators.FAVORITE_COLOR_CODE_RADIO_BUTTON,
}


class FormFieldsPage(BasePage):

    path = "/form-fields"

    def fill_form(
        self,
        name: str,
        email: str,
        password: str,
        favorite_drinks: list[str] | None = None,
        favorite_color: str | None = None,
        automation_option: str = "default",
    ):

        name_input = self.browser.find_element(*FormFieldsPageLocators.NAME_INPUT)
        self.scroll_to_element(name_input)
        name_input.send_keys(name)

        password_input = self.browser.find_element(
            *FormFieldsPageLocators.PASSWORD_INPUT
        )
        self.scroll_to_element(password_input)
        password_input.send_keys(password)

        if favorite_drinks:
            for drink in favorite_drinks:
                if drink.lower() in DRINK_MAP.keys():
                    locator = DRINK_MAP.get(drink.lower())
                    checkbox = self.browser.find_element(*locator)
                    self.scroll_to_element(checkbox)
                    checkbox.click()
                else:
                    raise ValueError(f"Unknown drink option provided: '{drink}'")

        if favorite_color:
            if favorite_color.lower() in COLOR_MAP.keys():
                locator = COLOR_MAP.get(favorite_color.lower())
                radio_button = self.browser.find_element(*locator)
                self.scroll_to_element(radio_button)
                radio_button.click()
            else:
                raise ValueError(f"Unknown color option provided: '{favorite_color}'")

        select_list = self.browser.find_element(
            *FormFieldsPageLocators.AUTOMATION_SELECT
        )
        self.scroll_to_element(select_list)
        select = Select(select_list)
        select.select_by_value(automation_option)

        email_input = self.browser.find_element(*FormFieldsPageLocators.EMAIL_INPUT)
        self.scroll_to_element(email_input)
        email_input.send_keys(email)

        message_input = self.browser.find_element(*FormFieldsPageLocators.MESSAGE_INPUT)
        self.scroll_to_element(message_input)

        script = """
            const list = arguments[0];
            const children = Array.from(list.children);
            const texts = children.map(c => c.innerText.trim());
            let longest = "";
            for (const t of texts) {
                if (t.length > longest.length) longest = t;
            }
            return [children.length, longest];
        """
        automation_tools_list = self.browser.find_element(
            *FormFieldsPageLocators.AUTOMATION_TOOLS_LIST
        )
        child_count, longest_tool = self.browser.execute_script(
            script, automation_tools_list
        )

        message_text = f"{child_count} {longest_tool}"
        message_input.send_keys(message_text)

        submit_button = self.browser.find_element(*FormFieldsPageLocators.SUBMIT_BUTTON)
        self.scroll_to_element(submit_button)
        submit_button.click()

    def success_alert_shown(self, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            assert (
                alert.text == "Message received!"
            ), f"Unexpected alert text: {alert.text}"
            alert.accept()
        except TimeoutException:
            assert False, "Alert not shown!"

    def success_alert_not_shown(self, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            text = alert.text
            alert.accept()
            assert False, f"Alert was shown unexpectedly with text: {text}"
        except TimeoutException:
            assert True
