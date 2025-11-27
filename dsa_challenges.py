# Function 1: filter_and_sort_evens
def filter_and_sort_evens(numbers):
    """Return a sorted list of even numbers from the input list."""
    evens = [num for num in numbers if num % 2 == 0]
    return sorted(evens)


# Function 2: count_character_frequency
def count_character_frequency(text):
    """Return a dictionary of character frequencies (case-insensitive)."""
    text = text.lower()
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


# Example calls to test the functions
if __name__ == "__main__":
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Even numbers sorted:", filter_and_sort_evens(numbers))

    text = "Hello World"
    print("Character frequencies:", count_character_frequency(text))
