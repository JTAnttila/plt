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

    # The input phrase can be a single word starting with a vowel. In that case, the translator applies to following translation rules:
    # If the word ends with "y", append “nay” to the and of the word.
    # If the word ends with a vowel, append “yay” to the and of the word.
    # If the word ends with a consonant, append “ay” to the and of the word.
    # The translation of “any” is “anynay”.
    def test_translate_single_word_starting_with_vowel(self):
        piglatin = PigLatin("any")
        self.assertEqual(piglatin.translate(), "anynay")

    # The translation of “apple” is “appleyay”.
    def test_translate_single_word_starting_with_vowel_ending_with_vowel(self):
        piglatin = PigLatin("apple")
        self.assertEqual(piglatin.translate(), "appleyay")

    # The translation of “ask” is “askay”.
    def test_translate_single_word_starting_with_vowel_ending_with_consonant(self):
        piglatin = PigLatin("ask")
        self.assertEqual(piglatin.translate(), "askay")
