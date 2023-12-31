# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fap4qouIdBYAV2e0xQiK9GlwrwaqpEUU
"""

# 1. What is a lambda function in Python, and how does it differ from a regular function?
'''Ans- In Python, a lambda function is a small, anonymous function that can have any number of arguments but can only have one expression. It is created using the lambda keyword and is often used for simple and short tasks where a full-fledged function definition is unnecessary.'''

'''Lambda functions are different from regular functions in several ways:
Anonymous: Lambda functions are anonymous, meaning they don't have a name like regular functions defined using the def keyword. They are generally used when you need a quick and temporary function without assigning it to a name.
'''

# 2. Can a lambda function in Python have multiple arguments? If yes, how can you define and use them?
'''
Yes, a lambda function in Python can have multiple arguments. The syntax for defining a lambda function with multiple arguments is:'''
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
sum_lists = map(lambda x, y: x + y, list1, list2)
print(list(sum_lists))

# 3. How are lambda functions typically used in Python? Provide an example use case.
'''
Lambda functions in Python are typically used in situations where a small, anonymous function is required for a short and simple task. They are commonly used in conjunction with higher-order functions like map, filter, and reduce, as well as in cases where a quick, throwaway function is needed without the need for a formal function definition.'''
# List of tuples (name, age)
people = [("Alice", 25), ("Bob", 20), ("Charlie", 30), ("David", 22)]

# Sorting the list of tuples based on the second element (age)
sorted_people = sorted(people, key=lambda person: person[1])

print(sorted_people)

# 4. What are the advantages and limitations of lambda functions compared to regular functions in Python?
'''
Advantages of Lambda Functions:

Conciseness: Lambda functions are concise and allow you to define simple, one-line functions quickly without the need for a full function definition using def.
Higher-Order Functions: Lambda functions work well with higher-order functions like map, filter, and reduce. They are often used as a quick way to provide a simple function for such functions.

Limitations of Lambda Functions:

Single Expression: Lambda functions can only contain a single expression. This limitation means they are not suitable for more complex tasks that require multiple statements or logic.
Limited Documentation: Without a name, lambda functions can make the code less self-documenting. Regular functions, on the other hand, can have meaningful names that provide hints about their purpose.'''

'''5. Are lambda functions in Python able to access variables defined outside of their own scope?
Explain with an example.'''

'''Yes, lambda functions in Python can access variables defined outside of their own scope. When a lambda function is created, it captures the values of the variables in the enclosing scope and retains access to those values even if the lambda function is called outside of that scope.'''

def outer_function():
    outer_variable = 10

    # Define a lambda function that uses the outer_variable
    inner_lambda = lambda x: x + outer_variable

    return inner_lambda

# Call the outer_function to get the lambda function
lambda_function = outer_function()

# Now, use the lambda_function with different values of x
result1 = lambda_function(5)
result2 = lambda_function(8)

print(result1)
print(result2)

# 6. Write a lambda function to calculate the square of a given number.
square = lambda x: x ** 2
result = square(5)
print(result)

# 7. Create a lambda function to find the maximum value in a list of integers.
find_max = lambda lst: max(lst)
numbers = [10, 5, 23, 17, 8, 30]
result = find_max(numbers)
print(result)

# 8. Implement a lambda function to filter out all the even numbers from a list of integers.
filter_even = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even(numbers)
print(even_numbers)

# 9. Write a lambda function to sort a list of strings in ascending order based on the length of each string'
sort_by_length = lambda lst: sorted(lst, key=lambda x: len(x))
strings = ["apple", "banana", "orange", "kiwi", "grape"]
sorted_strings = sort_by_length(strings)
print(sorted_strings)

'''
10. Create a lambda function that takes two lists as input and returns a new list containing the
common elements between the two lists.
'''
find_common_elements = lambda list1, list2: list(filter(lambda x: x in list2, list1))
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = find_common_elements(list1, list2)
print(common_elements)

# 11. Write a recursive function to calculate the factorial of a given positive integer.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(5)
print(result)

# 12. Implement a recursive function to compute the nth Fibonacci number.
def fibonacci(n):
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
result = fibonacci(10)
print(result)

# 13. Create a recursive function to find the sum of all the elements in a given list.
def recursive_sum(lst):
    if not lst:  # Base case: Empty list has sum 0
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])
numbers = [1, 2, 3, 4, 5]
result = recursive_sum(numbers)
print(result)

# 14. Write a recursive function to determine whether a given string is a palindrome.
def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase for case-insensitive comparison
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])
print(is_palindrome("racecar"))
print(is_palindrome("level"))
print(is_palindrome("hello"))
print(is_palindrome("Able was I ere I saw Elba"))

# 15. Implement a recursive function to find the greatest common divisor (GCD) of two positive integers.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(24, 18))
print(gcd(48, 60))
print(gcd(21, 14))

