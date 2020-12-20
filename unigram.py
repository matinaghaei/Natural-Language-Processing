class Unigram:

    def __init__(self):
        self.count = {}
        self.total = 0

    def add(self, word):
        if word in self.count:
            self.count[word] += 1
        else:
            self.count[word] = 1
        self.total += 1

    def count_word(self, word):
        if word in self.count:
            return self.count[word]
        return 0

    def get_probability(self, word):
        if word in self.count:
            return self.count[word] / self.total
        else:
            return 0
