import json
import requests

from django.test import TestCase

from tokenizer_challenge.settings import API_URL

class TokenizeTest(TestCase):

    def setUp(self):
        self.lang = "en"
        self.text = "Agent Smith: As you can see, we've had our eye on you for some time now, Mr. Anderson."
        self.tokens = [
            "Agent",
            "Smith",
            "As",
            "you",
            "can",
            "see",
            "we",
            "have",
            "had",
            "our",
            "eye",
            "on",
            "you",
            "for",
            "some",
            "time",
            "now",
            "Mr.",
            "Anderson"
        ]

    def test_tokenize_without_data(self):
        response = requests.get(f'{API_URL}/tokenizer/')
        self.assertEqual(response.status_code, 400)
        res_data = json.loads(response.content)
        self.assertEqual(res_data['error'], 'No data')

    def test_tokenize_without_text(self):
        req_data = {}
        response = requests.get(f'{API_URL}/tokenizer/', data=json.dumps(req_data))
        self.assertEqual(response.status_code, 400)
        res_data = json.loads(response.content)
        self.assertEqual(res_data['error'], 'No text')

    def test_tokenize_with_text(self):
        req_data = {'text': self.text}
        response = requests.get(f'{API_URL}/tokenizer/', data=json.dumps(req_data))
        self.assertEqual(response.status_code, 200)
        res_data = json.loads(response.content)
        self.assertEqual(res_data['tokens'], self.tokens)
        self.assertEqual(res_data['lang'], self.lang)

    def test_tokenize_with_language(self):
        req_data = {'lang': self.lang, 'text': self.text}
        response = requests.get(f'{API_URL}/tokenizer/', data=json.dumps(req_data))
        self.assertEqual(response.status_code, 200)
        res_data = json.loads(response.content)
        self.assertEqual(res_data['tokens'], self.tokens)
        self.assertEqual(res_data['lang'], self.lang)

    def test_tokenize_without_language(self):
        req_data = {'text': self.text}
        response = requests.get(f'{API_URL}/tokenizer/', data=json.dumps(req_data))
        self.assertEqual(response.status_code, 200)
        res_data = json.loads(response.content)
        self.assertEqual(res_data['tokens'], self.tokens)
        self.assertEqual(res_data['lang'], self.lang)

    def test_tokenize_with_bad_language(self):
        req_data = {'lang': 'test', 'text': self.text}
        response = requests.get(f'{API_URL}/tokenizer/', data=json.dumps(req_data))
        self.assertEqual(response.status_code, 400)
        res_data = json.loads(response.content)
        self.assertEqual(res_data['error'], 'Bad language. Alpha 2')
