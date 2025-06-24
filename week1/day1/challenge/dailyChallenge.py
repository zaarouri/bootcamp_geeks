number = int(input("Enter a number: "))
length = int(input("Enter the desired length: "))

multiples = [number * i for i in range(1, length + 1)]
print(multiples)    




# challenge gold 
word = input("Enter a word: ")

result = ""
for i in range(len(word)):
    if i == 0 or word[i] != word[i - 1]:
        result += word[i]

print(result)




