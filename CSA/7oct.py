
#07/10/2024

#palindrome number
def is_palindrome(s):  
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print('string is a palindrome.')
else:
    print('string is not a palindrome.')
    
#frequency string
def count_character_frequency(s):
    frequency = {}
    for char in s:
        if char != ' ':
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

input_string = input("enter array")
frequency_count = count_character_frequency(input_string)
print("Character frequencies:", frequency_count)

#substring occurance
def count_substring(main_string, substring):
    count = main_string.count(substring)
    return count


if __name__ == "__main__":
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring to count: ")
    
    occurrences = count_substring(main_string, substring)
    print(f"The substring '{substring}' occurs {occurrences} times in the main string.")


#swapping(1st and last character)
def swap_first_last(s):
    if len(s) <= 1:
        return s
    return s[-1] + s[1:-1] + s[0]


input_string = input("Enter a string: ")
swapped_string = swap_first_last(input_string)

print("Swapped string:", swapped_string)

#find longest word in string
def find_longest_word(s):
    words = s.split()
    longest_word = max(words, key=len)
    return longest_word

input_string = input("enter a string")
longest = find_longest_word(input_string)
print("The longest word is:", longest)