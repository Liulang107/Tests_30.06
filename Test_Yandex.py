# Задание 3. Применив selenium напишите unit-test для авторизации на Яндексе по url: https://passport.yandex.ru/auth/
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestYandexAuthPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_auth_on_Yandex(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/')

        login = driver.find_element_by_id('passp-field-login')
        login.send_keys('netologyzolotova')
        login.send_keys(Keys.ENTER)

        passwd = driver.find_element_by_id('passp-field-passwd')
        passwd.send_keys('netology')
        passwd.send_keys(Keys.ENTER)
        assert "Яндекс.Паспорт" in driver.title

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
