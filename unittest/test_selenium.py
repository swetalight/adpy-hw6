import time
import unittest
from selenium import webdriver


class YandexPassportTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
        self.test_login = 'test-yandex-login'
        self.test_passwd = 'password'
        self.people_delay = 3

    def test_page_passport(self):
        page_url = 'https://passport.yandex.ru/auth/'
        driver = self.driver
        driver.maximize_window()
        driver.get(page_url)

        ele_user_message = driver.find_element_by_id("passp-field-login")
        ele_user_message.clear()
        ele_user_message.send_keys(self.test_login)

        time.sleep(self.people_delay)

        login_btn = driver.find_element_by_css_selector('div > .button2_type_submit')
        login_btn.click()

        time.sleep(self.people_delay)

        user_passwd_input = driver.find_element_by_id('passp-field-passwd')
        user_passwd_input.send_keys(self.test_passwd)

        login_btn = driver.find_element_by_css_selector('div > .button2_type_submit')
        login_btn.click()

        time.sleep(self.people_delay)

        user_login_elem_first = driver.find_element_by_css_selector('div > .passp-account-list-item__display-name')

        if user_login_elem_first:
            user_test_text = user_login_elem_first.text
        else:
            user_login_elem_second = driver.find_element_by_css_selector('div > .personal-info-login__displaylogin')
            user_test_text = user_login_elem_second.text

        self.assertEqual(self.test_login, user_test_text)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
