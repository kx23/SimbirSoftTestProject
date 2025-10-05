from ..pages.form_fields_page import FormFieldsPage
import pytest


valid_fill_data = [
    (
        "Harutyunyan Artavazd",
        "myemail@dom.com",
        "PassW0rd@11",
        ["Milk", "Coffee"],
        "Yellow",
        "yes",
    )
]

invalid_fill_data = [
    (
        "",
        "myemail@dom.com",
        "PassW0rd@11",
        ["Milk", "Coffee"],
        "Yellow",
        "yes",
    )
]


class TestFormFieldsPage:

    @pytest.mark.parametrize(
        "name, email, password, favorite_drinks, favorite_color, automation_option",
        valid_fill_data,
    )
    @pytest.mark.need_review
    def test_submit_form_with_valid_data(
        self,
        browser,
        name: str,
        email: str,
        password: str,
        favorite_drinks: list[str],
        favorite_color: str,
        automation_option: str,
    ):
        page = FormFieldsPage(browser)
        page.open()
        page.fill_form(
            name, email, password, favorite_drinks, favorite_color, automation_option
        )
        page.success_alert_shown()

    @pytest.mark.parametrize(
        "name, email, password, favorite_drinks, favorite_color, automation_option",
        invalid_fill_data,
    )
    @pytest.mark.need_review
    def test_submit_form_with_invalid_data(
        self,
        browser,
        name: str,
        email: str,
        password: str,
        favorite_drinks: list[str],
        favorite_color: str,
        automation_option: str,
    ):
        page = FormFieldsPage(browser)
        page.open()
        page.fill_form(
            name, email, password, favorite_drinks, favorite_color, automation_option
        )
        page.success_alert_not_shown()
