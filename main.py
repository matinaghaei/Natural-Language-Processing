from train import Train
from test import Test

unigram_factor = float(input("Enter Unigram Factor: "))
bigram_factor = float(input("Enter Bigram Factor: "))

train_file = open("HAM-Train.txt", mode="r", encoding="utf-8")
test_file = open("HAM-Test.txt", mode="r", encoding="utf-8")

train = Train(train_file.read().split('\n'), unigram_factor, bigram_factor)
train.train()
test = Test(test_file.read().split('\n'), train.get_languages())
test.test()
test.print_result()
