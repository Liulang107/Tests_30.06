# Задание 3. Применив selenium напишите unit-test для авторизации на Яндексе по url: https://passport.yandex.ru/auth/

# Уже отправила на допроверку, но внесла еще изменений, не могу прикрепить новый комментарий к домашке:
# - нашла проблему в драйвере; с помощью библиотеки установился верный и все сразу заработало.
# Чтобы при каждом запуске кода, этот менеджер не пытался каждый раз загружать драйвер, заменила далее его на путь;
# - как понимаю прежде чем загрузить первую страницу, грузится промежуточная с тайтлом Авторизация: так работает работает тест
# правильно я понимаю, здесь должен быть какой-то таймаут, который должен догрузить вторую страницу, где тайтл Яндекс.Паспорт?
# Как сделать это?


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager


class TestYandexAuthPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/Maria/.wdm/chromedriver/75.0.3770.90/mac64/chromedriver')
        self.driver.implicitly_wait(20)

    def test_auth_on_Yandex(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/')

        login = driver.find_element_by_id('passp-field-login')
        login.send_keys('netologyzolotova')
        login.send_keys(Keys.ENTER)

        passwd = driver.find_element_by_id('passp-field-passwd')
        passwd.send_keys('netology')
        passwd.send_keys(Keys.ENTER)
        assert "Авторизация" in driver.title

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
