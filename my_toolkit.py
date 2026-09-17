
def calculate_average(numbers):
    # This is calculate the average of a list of numbers
    if len(numbers) == 0: 
        return 0

    total = 0

    for number in numbers:
        total += number 

    return total / len(numbers)

def find_max_and_min(numbers):
    #This returns a tuple contianing maximum and minimum in a list
    if len(numbers) == 0:
        return (None, None)

    max_value = numbers[0]
    min_value = numbers[0]

    for number in numbers:
        if number > max_value:
            max_value = number

        if number < min_value:
            min_value = number

    return (max_value, min_value)

def count_occurrences(items, target):
    #This is to return number of times a target appears in a list
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count 

def is_palindrome(text):
    #This returns true if text reads forward and backwards
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1] 

def create_report(title, scores): 
    #This prints a formatted report with average, and maximum and minimum value
    average = calculate_average(scores)
    max_value, min_value = find_max_and_min(scores)

    report = (
        f"{title}\n"
        f"Average: {average:.2f}\n"
        f"Highest: {max_value}\n"
        f"Lowest: {min_value}"
    )
    return report 


if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]
    
    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))


# Edge cases
print("\n--- Edge Cases ---\n")

# For empty list avaerage, and max and min value
print("Empty average:", calculate_average([]))
print("Empty max/min:", find_max_and_min([]))

# For target appearance multiple times
numbers = [7, 7, 3, 7, 9, 7]
print("Count of 7:", count_occurrences(numbers, 7))
print("Count of 10:", count_occurrences(numbers, 10))

# For spaces and mixed case Palindrome
print("Phrase palindrome:", is_palindrome("A man a plan a canal Panama"))

# For Single character Palindrome
print("Single character palindrome:", is_palindrome("a"))

# For Mixed-case Palindrome
print("Mixed case palindrome:", is_palindrome("RaceCar"))

