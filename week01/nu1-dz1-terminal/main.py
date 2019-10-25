import random

words = ['neural', 'random', 'python', 'hello', 'lesson_05']

words_choices = random.sample(words, random.randint(1, 3))

text = str(random.randint(1, 9)).join(words_choices)

print(text)
