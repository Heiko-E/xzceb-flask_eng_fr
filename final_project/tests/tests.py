import unittest

from machinetranslaton import translator


class TestSquare(unittest.TestCase):

    def test_english_to_french(self):
        english_text = 'Hello'
        french_text = translator.english_to_french(english_text)
        self.assertEqual(french_text, 'Bonjour')

    def test_french_to_english(self):
        french_text = 'Bonjour'
        english_text = translator.french_to_english(french_text)
        self.assertEqual(english_text, 'Hello')


if __name__ == '__main__':
    unittest.main()
