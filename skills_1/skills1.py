# Things you should be able to do. #start = 9:14 end = 9:21 on October 5, 2014
# Write a function that takes a list and returns a new list with only the odd numbers.
some_list = [3, 4, 2, 1, 5, 6]
some_list2 = [3, 4, 2, 1, 5, 6]
word_list = ["apple", "bit", "saucy", "red", "core", "seed", "new"]
string_list = ["I", "went", "dancing", "last", "night."]
numbers = [2, 4, 6, 8]

def all_odd(some_list):
    odds = []
    for i in some_list:
        if i % 2 != 0:
            odds.append(i)
    return odds



# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    evens = []
    for i in some_list:
        if i % 2 == 0:
            evens.append(i)
    return evens



# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    longer = []
    for i in word_list:
        if len(i) >= 4:
            longer.append(i)
    return longer



# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    some_list.sort()
    return some_list[0]


# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    return max(some_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    half = []
    for i in some_list:
        half = half + [(i/2.0)]
    return half

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    lengths = []
    for i in word_list:
        lengths = lengths + [len(i)]
    return lengths

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    product = 1
    for i in numbers:
        product = product * i
    return product

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    new_str = ""
    count = 0
    length = len(string_list)
    for i in string_list:
        count += 1
        if count < length:
            new_str = new_str + i + " "
        else:
            new_str = new_str + i
    return new_str

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    return sum(numbers) / len(numbers)
