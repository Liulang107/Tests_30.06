# Задание 2. Проверим актуальность API Яндекс.Переводчик'а для потенциального сервиса переводов.
# Используя библиотеку request напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
#
# Пример положительных тестов:
#
# Код ответа соответствует 200
# результат перевода правильный - "привет"

import unittest
import requests


class TestYandexAPI(unittest.TestCase):
    def setUp(self):
        self.API_KEY = 'trnsl.1.1.20190505T182807Z.f6dbdddd0edd52a9.f07fa2f49c932fc97866472295fd1cd1b4a565cc'
        self.URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        self.params = {
            'key': self.API_KEY,
            'text': 'hi',
            'lang': 'en-ru'
        }

    def test_translate_hi(self):
        response = requests.get(self.URL, self.params)
        result = ''.join(response.json()['text'])
        self.assertEqual(result, 'привет')

    def test_translate_hi_response_code(self):
        response = requests.get(self.URL, self.params)
        result = response.json()['code']
        self.assertEqual(result, 200)

    @unittest.expectedFailure
    def test_translate_it_wrong_arguments(self):
        self.params['text'] = 'hola'
        response = requests.get(self.URL, self.params)
        result = ''.join(response.json()['text'])
        self.assertEqual(result, 'привет')


if __name__ == '__main__':
    unittest.main()
