import requests
import unittest


def translate_text(text):
    token = 'trnsl.1.1.20190625T125517Z.b15a46ad85ecdc9e.d6655e0ea25a46cac2c51511793586c6fa1c9853'
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    web_req = requests.get(url, params={
        'key': token, 'lang': 'en-ru', 'text': text
    })

    return web_req.json()


class YandexTranslateTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.translate_dict = translate_text('hi')

    def test_url_availabeled_success(self):
        req_code = self.translate_dict['code']
        self.assertTrue((200 <= req_code < 300))

    def test_url_availabeled_failed(self):
        req_code = self.translate_dict['code']
        self.assertFalse((req_code < 200 or req_code >= 300))

    def test_translated_text(self):
        translated_text = set(self.translate_dict['text'])
        self.assertTrue(('привет' in translated_text))


if __name__ == '__main__':
    unittest.main()
