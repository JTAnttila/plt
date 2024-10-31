class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"

        words = self.phrase.split()
        translated_words = []

        for word in words:
            subwords = word.split('-')
            translated_subwords = []

            for subword in subwords:
                if subword[0].lower() in 'aeiou':
                    if subword[-1].lower() == 'y':
                        translated_subwords.append(subword + "nay")
                    elif subword[-1].lower() in 'aeiou':
                        translated_subwords.append(subword + "yay")
                    else:
                        translated_subwords.append(subword + "ay")
                else:
                    consonant_cluster = ""
                    for char in subword:
                        if char.lower() not in 'aeiou':
                            consonant_cluster += char
                        else:
                            break
                    translated_subwords.append(subword[len(consonant_cluster):] + consonant_cluster + "ay")

            translated_words.append('-'.join(translated_subwords))

        return ' '.join(translated_words)