import unittest
from translator import french_to_english,english_to_french

class TestSquare(unittest.TestCase):

    def test_english_to_french(self):
        english_text='Hello'
        french_text= english_to_french(english_text)
        self.assertEqual(french_text, 'Bonjour')

    def test_french_to_english(self):
        french_text= 'Bonjour'
        english_text=french_to_english(french_text)
        self.assertEqual(english_text, 'Hello')