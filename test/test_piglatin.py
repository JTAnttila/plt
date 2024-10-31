import unittest
from piglatin import PigLatin


class TestPigLatin(unittest.TestCase):

    # The translator takes as the input the phrase “hello world”. Anyone gets the input phrase: “hello world”.
    def test_get_phrase(self):
        piglatin = PigLatin("hello world")
        self.assertEqual(piglatin.get_phrase(), "hello world")
