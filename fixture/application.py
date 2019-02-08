__autor__ = 'Dmitrii Dubrovskii'
from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def is_session_valid(self):
        try:
            self.wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='home'])[1]/preceding::a[3]")
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if (wd.current_url):
            wd.get(self.base_url)
        else:
            pass

    def destroy(self):
        self.wd.quit()