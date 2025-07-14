# Exercise 1: Return the Largest Number
def find_largest(numbers):
    """
    Takes a list of numbers and returns the largest number.
    
    Args:
        numbers (list): A list of numbers
    
    Returns:
        int/float: The largest number in the list
    """
    return max(numbers)

# Alternative implementation without using max()
def find_largest_alternative(numbers):
    """
    Alternative implementation that finds the largest number manually.
    """
    if not numbers:  
        return None
    
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


# Exercise 2: Check for Letter in Word
def check_letter(word, letter):
    """
    Checks if a letter is present in a word.
    
    Args:
        word (str): The word to search in
        letter (str): The letter to search for
    
    Returns:
        bool: True if letter is found, False otherwise
    """
    return letter in word

# Alternative implementation using a loop
def check_letter_alternative(word, letter):
    """
    Alternative implementation that checks each character manually.
    """
    for char in word:
        if char == letter:
            return True
    return False


# Exercise 3: Count to a Number
def count_to_number(n):
    """
    Prints all numbers from 1 to n (inclusive).
    
    Args:
        n (int): The number to count up to
    """
    for i in range(1, n + 1):
        print(i)

# Alternative implementation using while loop
def count_to_number_alternative(n):
    """
    Alternative implementation using a while loop.
    """
    i = 1
    while i <= n:
        print(i)
        i += 1


# Test the functions
if __name__ == "__main__":
    print("=== Exercise 1: Find Largest ===")
    print(find_largest([1, 2, 3, 4])) 
    print(find_largest([10, 20, 5]))   
    print(find_largest([-1, -5, -2]))  
    
    print("\n=== Exercise 2: Check Letter ===")
    print(check_letter("apple", "a"))   
    print(check_letter("banana", "z"))  
    print(check_letter("hello", "l"))   
    
    print("\n=== Exercise 3: Count to Number ===")
    print("Counting to 3:")
    count_to_number(3)
    
    print("\nCounting to 5:")
    count_to_number(5)