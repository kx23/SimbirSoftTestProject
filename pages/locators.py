from selenium.webdriver.common.by import By


class FormFieldsPageLocators:
    NAME_INPUT = (By.ID, "name-input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input#email")
    MESSAGE_INPUT = (By.CSS_SELECTOR, "textarea#message")

    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button#submit-btn")

    FAVORITE_DRINK_WATER_CHECKBOX = (
        By.CSS_SELECTOR,
        'input[value="Water"][name="fav_drink"]',
    )
    FAVORITE_DRINK_MILK_CHECKBOX = (
        By.CSS_SELECTOR,
        'input[value="Milk"][name="fav_drink"]',
    )
    FAVORITE_DRINK_COFFEE_CHECKBOX = (
        By.CSS_SELECTOR,
        'input[value="Coffee"][name="fav_drink"]',
    )
    FAVORITE_DRINK_WINE_CHECKBOX = (
        By.CSS_SELECTOR,
        'input[value="Wine"][name="fav_drink"]',
    )
    FAVORITE_DRINK_CTRL_ALT_DELIGHT_CHECKBOX = (
        By.CSS_SELECTOR,
        'input[value="Ctrl-Alt-Delight"][name="fav_drink"]',
    )

    FAVORITE_COLOR_RED_RADIO_BUTTON = (
        By.CSS_SELECTOR,
        'input[value="Red"][name="fav_color"]',
    )
    FAVORITE_COLOR_BLUE_RADIO_BUTTON = (
        By.CSS_SELECTOR,
        'input[value="Blue"][name="fav_color"]',
    )
    FAVORITE_COLOR_YELLOW_RADIO_BUTTON = (
        By.CSS_SELECTOR,
        'input[value="Yellow"][name="fav_color"]',
    )
    FAVORITE_COLOR_GREEN_RADIO_BUTTON = (
        By.CSS_SELECTOR,
        'input[value="Green"][name="fav_color"]',
    )
    FAVORITE_COLOR_CODE_RADIO_BUTTON = (
        By.CSS_SELECTOR,
        'input[value="Ctrl-Alt-Delight"][name="#FFC0CB"]',
    )

    AUTOMATION_SELECT = (By.CSS_SELECTOR, "select#automation")
    AUTOMATION_OPTION_DEFAULT = "default"
    AUTOMATION_OPTION_YES = "yes"
    AUTOMATION_OPTION_NO = "no"
    AUTOMATION_OPTION_UNDECIDED = "undecided"

    AUTOMATION_TOOLS_LIST = (
        By.XPATH,
        '//label[text()="Automation tools"]/following-sibling::ul',
    )
