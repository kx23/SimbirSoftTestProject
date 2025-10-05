from urllib.parse import urljoin


class BasePage:
    base_url = "https://practice-automation.com"
    path = ""

    def __init__(self, browser, url=None, timeout=3):
        self.browser = browser
        if url:

            self.url = url if "://" in url else urljoin(self.base_url, url)
        else:
            self.url = urljoin(self.base_url, self.path)
        self.browser.implicitly_wait(timeout)

    def open(self):
        print(self.url)
        self.browser.get(self.url)

    def scroll_to_element(self, element):
        self.browser.execute_script(
            "return arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});",
            element,
        )
