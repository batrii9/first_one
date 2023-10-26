with open("story.txt", "r") as f:
    story = f.read()
words = set()
start_of_word = -1
for i, char in enumerate(story):
    if char == "<":
        start_of_word = i
    if char == ">" and start_of_word != -1:
        word = story[start_of_word: i+1]
        words.add(word)
        start_of_word = -1
answers = {}
for word in words:
    answer = input("give a word for " + word + ": ")
    answers[word] = answer
for word in words:
    story = story.replace(word, answers[word])
print("")
print(story)