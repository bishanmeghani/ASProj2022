sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR \
YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"

word = "ask"

def task1(word, sentence):
    word = word.lower()
    sentence = sentence.lower()
    sentence = sentence.split()
    positions = []
    for i in range(len(sentence)):
        if sentence[i] == word:
            positions.append(i+1)
    return positions

print(task1(word, sentence))