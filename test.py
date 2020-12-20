class Test:

    def __init__(self, testing_data, languages):
        self.table = {}
        self.precision = {}
        self.recall = {}
        self.f_measure = {}
        self.testing_data = testing_data
        self.languages = languages
        for language in languages:
            self.table[language] = {}

    def test(self):
        progress = 0
        percentage = 0
        for tt in self.testing_data:
            title, text = tt.split("@@@@@@@@@@ ")
            self.recall[title] = None
            predicted = self.predict(text)
            if title in self.table[predicted]:
                self.table[predicted][title] += 1
            else:
                self.table[predicted][title] = 1
            progress += 1
            if int(progress / len(self.testing_data) * 10) > int(percentage * 10):
                percentage = progress / len(self.testing_data)
                print("testing {}%".format(int(percentage * 100)))
        self.calculate_precision()
        self.calculate_recall()
        self.calculate_f_measure()

    def calculate_precision(self):
        for predicted, actual_languages in self.table.items():
            total = 0
            correct = 0
            for actual, times in actual_languages.items():
                if predicted == actual:
                    correct += times
                total += times
            if total != 0:
                self.precision[predicted] = correct / total

    def calculate_recall(self):
        for actual in self.recall:
            total = 0
            recalled = 0
            for predicted, actual_languages in self.table.items():
                if actual in actual_languages:
                    times = actual_languages[actual]
                    if predicted == actual:
                        recalled += times
                    total += times
            self.recall[actual] = recalled / total

    def calculate_f_measure(self):
        for c in self.precision:
            if c in self.recall:
                self.f_measure[c] = 2 * self.precision[c] * self.recall[c] / (self.precision[c] + self.recall[c])

    def predict(self, text):
        best = {"Language": None, "Probability": None}
        for title, language in self.languages.items():
            probability = language.get_text_probability(text)
            if best["Probability"] is None or probability > best["Probability"]:
                best["Language"], best["Probability"] = title, probability
        return best["Language"]

    def print_result(self):
        print("Precision: ", self.precision)
        print("Recall: ", self.recall)
        print("F-measure: ", self.f_measure)
