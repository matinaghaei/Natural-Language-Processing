class Bigram:

    def __init__(self, unigram):
        self.unigram = unigram
        self.count = {}
        self.total = 0

    def add(self, word1, word2):
        w = word1 + " " + word2
        if w in self.count:
            self.count[w] += 1
        else:
            self.count[w] = 1
        self.total += 1

    def get_probability(self, word1, word2):
        w = word1 + " " + word2
        if w in self.count:
            return self.count[w] / self.unigram.count_word(word1)
        else:
            return 0
