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

    # The input phrase can be a single word starting with a single consonant (note that the "y" letter is considered a consonant). In that case, the translator applies the following translation rule:
    # Remove the consonant from the beginning of the word and add it to the end of the word. Finally, append “ay” to the end of the resulting word.
    # The translation of “hello” is “ellohay”.
    def test_translate_single_word_starting_with_consonant(self):
        piglatin = PigLatin("hello")
        self.assertEqual(piglatin.translate(), "ellohay")

    # The input phrase can be a single word starting with more consonants. In that case, the translator applies the following translation rule:
    # Remove the consonants from the beginning of the word and add them to the end of the word. Finally, append “ay” to the end of the resulting word.
    # The translation of “known” is “ownknay”.
    def test_translate_single_word_starting_with_more_consonants(self):
        piglatin = PigLatin("known")
        self.assertEqual(piglatin.translate(), "ownknay")

    # The input phrase can contain more words (separated by white spaces). In that case, the translator applies the translation rules (reported in User Stories 3-5) to the single words. Moreover, for composite words (those separated by a “-”), the translation rules apply to the single words.
    # The translation of “hello world” is “ellohay orldway”.
    def test_translate_multiple_words(self):
        piglatin = PigLatin("hello world")
        self.assertEqual(piglatin.translate(), "ellohay orldway")

    # Implement PigLatin.translate(self) -> str to let the translator translate a phrase containing more words, as well as composite words.
    # The translation of “well-being” is “ellway-eingbay”
    def test_translate_composite_words(self):
        piglatin = PigLatin("well-being")
        self.assertEqual(piglatin.translate(), "ellway-eingbay")

    # The input phrase can contain punctuation marks. In that case, the translator applies the translation rules to the single and composite words while preserving the punctuation marks. Only the following punctuation marks are allowed: point, comma, semi-colon, colon, apostrophe, question mark, exclamation mark, and round parenthesis.
    # Implement PigLatin.translate(self) -> str to let the translator translate a phrase containing the allowed punctuation marks. For punctuation marks not allowed, raise a PigLatinError.
    # The translation of “hello world!” is “ellohay orldway!”.
    def test_translate_punctuation_marks(self):
        piglatin = PigLatin("hello world!")
        # take account that the punctuation mark is not allowed then create an error into error.py to pass this test
        self.assertEqual(piglatin.translate(), "ellohay orldway!")

    # The input phrase can contain upper- and title-case words. In those cases, the translator applies the translation rules to the single and composite words while preserving the upper- and title-cases. Cases different from upper- and title-cases are not allowed (e.g., “biRd”).
    # Requirement: Implement PigLatin.translate(self) -> str to let the translator translate a phrase containing upper- and title-case words. For cases different from upper- and title-cases, raise a PigLatinError.
    # The translation of “APPLE” (upper case) is “APPLEYAY”.
    def test_translate_upper_case(self):
        piglatin = PigLatin("APPLE")
        # take account that the case is not allowed then create an error into error.py to pass this test
        self.assertEqual(piglatin.translate(), "APPLEYAY")


