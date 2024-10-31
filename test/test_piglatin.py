import unittest
from piglatin import PigLatin


class TestPigLatin(unittest.TestCase):

    # The translator takes as the input the phrase “hello world”. Anyone gets the input phrase: “hello world”.
    def test_get_phrase(self):
        piglatin = PigLatin("hello world")
        self.assertEqual(piglatin.get_phrase(), "hello world")

    # The translator translates an input phrase into Pig Latin. The input phrase can be an empty string. When this happens, the result of the translation is “nil”.
    # The translation of an empty string is “nil”.
    def test_translate_empty_string(self):
        piglatin = PigLatin("")
        self.assertEqual(piglatin.translate(), "nil")
