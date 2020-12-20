from language import Language


class Train:

    def __init__(self, training_data, unigram_factor, bigram_factor):
        self.languages = {}
        self.training_data = training_data
        self.unigram_factor = unigram_factor
        self.bigram_factor = bigram_factor

    def train(self):
        progress = 0
        percentage = 0
        for td in self.training_data:
            title, text = td.split("@@@@@@@@@@ ")
            if title in self.languages:
                self.languages[title].add_text(text)
            else:
                self.languages[title] = Language(text, self.unigram_factor, self.bigram_factor)
            progress += 1
            if int(progress / len(self.training_data) * 10) > int(percentage * 10):
                percentage = progress / len(self.training_data)
                print("training {}%".format(int(percentage * 100)))

    def get_languages(self):
        return self.languages
