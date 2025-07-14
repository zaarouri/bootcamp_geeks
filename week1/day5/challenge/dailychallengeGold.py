def sort_words():
    words = input("Enter words (comma separated): ")
    sorted_words = sorted([word.strip() for word in words.split(",")])
    print(",".join(sorted_words))

# Example:
# Input: without,hello,bag,world
# Output: bag,hello,without,world

sort_words()

def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

# Test examples
print(longest_word("Margaret's toy is a pretty doll."))            # ➞ "Margaret's"
print(longest_word("A thing of beauty is a joy forever."))         # ➞ "forever."
print(longest_word("Forgetfulness is by all means powerless!"))    # ➞ "Forgetfulness"
