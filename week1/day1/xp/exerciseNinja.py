# Exercise 1 
# 3 <= 3 < 9       # True
# 3 == 3 == 3      # True
# bool(0)          # False
# bool(5 == "5")   # False
# bool(4 == 4) == bool("4" == "4")   # True
# bool(bool(None)) # False

# x = (1 == True)      # True
# y = (1 == False)     # False
# a = True + 4         # 5
# b = False + 10       # 10

# print("x is", x)     # x is True
# print("y is", y)     # y is False
# print("a:", a)       # a: 5
# print("b:", b)       # b: 10


# Exercise 2: 

longest_sentence = ""

while True:
    sentence = input("Enter the longest sentence you can without the character 'A':  , type exit to stop")
    if sentence == 'exit':
        break
    if 'a' in sentence.lower():
        print("Oops! Your sentence contains the letter 'A'. Try again.\n")
        continue

    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congratulations! You've set a new record!\n")
    else:
        print("Nice try, but not longer than your previous best.\n")
        
        
        
# Exercise 3
paragraph = "Artificial intelligence is the ability of machines to perform tasks typically associated with human intelligence, such as learning, reasoning, problem solving, perception, or decision-making."

import re

total_chars = len(paragraph)
non_whitespace_chars = len(paragraph.replace(" ", "").replace("\n", ""))

sentences = paragraph.split(",")
sentences = [s.strip() for s in sentences if s.strip()]
sentence_count = len(sentences)

words = re.findall(r'\b\w+\b', paragraph.lower())
word_count = len(words)
unique_words = set(words)
unique_word_count = len(unique_words)
non_unique_word_count = word_count - unique_word_count

average_words_per_sentence = word_count / sentence_count if sentence_count else 0

print("Paragraph Analysis")
print("-" * 30)
print(f"Total characters: {total_chars}")
print(f"Non-whitespace characters: {non_whitespace_chars}")
print(f"Total sentences (split by commas): {sentence_count}")
print(f"Total words: {word_count}")
print(f"Unique words: {unique_word_count}")
print(f"Non-unique words: {non_unique_word_count}")
print(f"Average words per sentence: {average_words_per_sentence:.2f}")