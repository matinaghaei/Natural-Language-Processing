from unigram import Unigram
from bigram import Bigram
import math


class Language:

    def __init__(self, text, unigram_factor, bigram_factor):
        self.unigram = Unigram()
        self.bigram = Bigram(self.unigram)
        self.unigram_factor = unigram_factor
        self.bigram_factor = bigram_factor
        self.add_text(text)

    def add_text(self, text):
        words = text.split(' ')
        self.unigram.add(" ")
        self.unigram.add(words[0])
        self.bigram.add(" ", words[0])
        for i in range(1, len(words)):
            self.unigram.add(words[i])
            self.bigram.add(words[i - 1], words[i])

    def get_probability(self, word1, word2):
        return self.unigram.get_probability(word2) * self.unigram_factor\
               + self.bigram.get_probability(word1, word2) * self.bigram_factor\
               + (1 - self.unigram_factor - self.bigram_factor)

    def get_text_probability(self, text):
        probability = 0
        words = text.split(' ')
        probability += math.log2(self.get_probability(" ", words[0]))
        for i in range(1, len(words)):
            probability += math.log2(self.get_probability(words[i - 1], words[i]))
        return probability
