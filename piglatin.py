import re
from error import PigLatinError

class PigLatin:

    ALLOWED_PUNCTUATION = {'.', ',', ';', ':', '\'', '?', '!', '(', ')', '-'}

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"

        # Check for disallowed punctuation marks
        for char in self.phrase:
            if not char.isalnum() and char not in self.ALLOWED_PUNCTUATION and not char.isspace():
                raise PigLatinError(f"Disallowed punctuation mark: {char}")

        words = re.findall(r'\b\w+[-\w]*\b|[^\w\s]', self.phrase)
        translated_words = []

        for word in words:
            if re.match(r'\w', word):
                if '-' in word:
                    subwords = word.split('-')
                    translated_subwords = [self._translate_word(subword) for subword in subwords]
                    translated_words.append('-'.join(translated_subwords))
                else:
                    translated_words.append(self._translate_word(word))
            else:
                translated_words.append(word)

        # Join words with spaces, preserving punctuation marks
        result = ''.join(
            ' ' + word if re.match(r'\w', word) else word for word in translated_words
        ).strip()
        return result

    def _translate_word(self, word: str) -> str:
        if word[0].lower() in 'aeiou':
            if word[-1].lower() == 'y':
                return word + "nay"
            elif word[-1].lower() in 'aeiou':
                return word + "yay"
            else:
                return word + "ay"
        else:
            consonant_cluster = ""
            for char in word:
                if char.lower() not in 'aeiou':
                    consonant_cluster += char
                else:
                    break
            return word[len(consonant_cluster):] + consonant_cluster + "ay"