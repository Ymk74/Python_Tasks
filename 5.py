#Create a function that takes a sentence and prints how many words in the sentence (do not count the spaces)
sentence = input('Enter Sentence:')
def word_count(sentence):
    return len(sentence.split())


count = word_count(sentence)
print (count)
