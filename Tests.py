# Задание 1. Необходимо протестировать программу по работе с бухгалтерией
#
# Следует протестировать основные функции по получению информации о документах,
# добавлении и удалении элементов из словаря.
# Используйте fixture для загрузки данных в тестовый класс

import unittest
import os
import json
from io import StringIO
import sys
from mock import patch
from src import app


class TestSecretaryProgram(unittest.TestCase):

    def setUp(self):
        current_path = str(os.path.dirname(os.path.abspath(__file__)))
        f_directories = os.path.join(current_path, 'src/fixtures/directories.json')
        f_documents = os.path.join(current_path, 'src/fixtures/documents.json')
        with open(f_documents, 'r') as out_docs:
            app.documents = json.load(out_docs)
        with open(f_directories, 'r') as out_dirs:
            app.directories = json.load(out_dirs)

    def test_get_all_doc_owners_names(self):
        self.assertTrue(app.get_all_doc_owners_names())

    @patch('builtins.input', lambda x: '11-2')
    def test_get_doc_owner_name(self):
        self.assertEqual(app.get_doc_owner_name(), "Геннадий Покемонов")

    @patch('builtins.input', lambda x: '1111')
    def test_get_doc_owner_name(self):
        self.assertFalse(app.get_doc_owner_name())

    def test_show_all_docs_info(self):
        sys.stdout = mystdout = StringIO()
        app.show_all_docs_info()
        self.assertTrue(mystdout.getvalue())

    @patch('builtins.input', lambda x: '11-2')
    def test_get_doc_shelf(self):
        self.assertEqual(app.get_doc_shelf(), '1')

    @patch('builtins.input', lambda x: '5')
    def test_add_new_doc(self):
        self.assertEqual(app.add_new_doc(), '5')

    @patch('builtins.input', lambda x: '11-2')
    def test_delete_doc(self):
        app.delete_doc()
        self.assertNotIn('11-2', app.documents)
        self.assertNotIn('11-2', app.directories)

    @patch('builtins.input', lambda x: '10006')
    def test_move_doc_to_shelf(self):
        app.move_doc_to_shelf()
        self.assertIn('10006', app.directories['10006'])

    def test_add_new_shelf(self):
        app.add_new_shelf('500')
        self.assertIn('500', app.directories)

    @patch('builtins.input', lambda x: 'q')
    def test_secretary_program_start(self):
        self.assertFalse(app.secretary_program_start())


if __name__ == '__main__':
    unittest.main(buffer=True)


# Задание 2. Проверим актуальность API Яндекс.Переводчик'а для потенциального сервиса переводов.
# Используя библиотеку request напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
#
# Пример положительных тестов:
#
# Код ответа соответствует 200
# результат перевода правильный - "привет"

import requests


def translate_it(text, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    API_KEY = 'trnsl.1.1.20190505T182807Z.f6dbdddd0edd52a9.f07fa2f49c932fc97866472295fd1cd1b4a565cc'
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang)
    }

    global response
    response = requests.get(URL, params=params)
    result = ''.join(response.json()['text'])

    return result


class TestYandexAPI(unittest.TestCase):
    def test_translate_it(self):
        self.assertEqual(translate_it(text='hi', from_lang='en'), 'привет')

    def test_translate_it_response_code(self):
        translate_it(text='hi', from_lang='en')
        self.assertEqual(response.json()['code'], 200)

    @unittest.expectedFailure
    def test_translate_it_wrong_arguments(self):
        self.assertEqual(translate_it(text='hi', from_lang='de'), 'привет')


if __name__ == '__main__':
    unittest.main()

# Задание 3. Применив selenium напишите unit-test для авторизации на Яндексе по url: https://passport.yandex.ru/auth/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

