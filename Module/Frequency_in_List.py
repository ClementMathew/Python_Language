from collections import Counter

def frequency_of_elements(lst):
    return Counter(lst)

# Example usage:
numbers = [5, 3, 9, 7, 3, 9, 5, 1]
print("Frequency of elements:", frequency_of_elements(numbers))
