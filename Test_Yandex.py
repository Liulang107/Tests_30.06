# Задание 3. Применив selenium напишите unit-test для авторизации на Яндексе по url: https://passport.yandex.ru/auth/

from selenium import webdriver

class TestYandexAuthPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/Maria/Desktop/chromedriver")
        self.driver.implicitly_wait(10)

    def test_auth_on_Yandex(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/')

        login = driver.find_element_by_id('passp-field-login')
        login.send_keys('netologyzolotova')

        driver.find_element_by_css_selector('button.control button2 button2_view_classic '
                                            'button2_size_l button2_theme_action button2_width_max '
                                            'button2_type_submit passp-form-button').click()

        passwd = driver.find_element_by_id('passp-field-passwd')
        passwd.send_keys('netology')

        driver.find_element_by_css_selector('button.control button2 button2_view_classic '
                                            'button2_size_l button2_theme_action button2_width_max '
                                            'button2_type_submit passp-form-button').click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

