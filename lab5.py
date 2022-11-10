'''2) Create a function and an anonymous function that receive a variable number of arguments. Both will return the
sum of the values of the keyword arguments.
Example:
For the call my_function(1, 2, c=3, d=4) the returned value will be 7.'''

def ex2(*params, **dict_params):
    res = 0
    for num in dict_params.values():
        res += num
    return res


print(ex2(1, 2, c=3, d=4))
f = lambda *params, **dict_params: sum(dict_params.values())

print(f(1, 2, c=3, d=4))


'''3) Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate a list
with all the vowels in a given string.
For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].'''
def ex3(string):
    res = []
    for char in string:
        if char in "AEIOUaeiou":
            res.append(char)
    return res


print(ex3("Programming in Python is fun"))
string = "Programming in Python is fun iii"
print([char for char in string if char in "AEIOUaeiou"])
print(list(filter(lambda x: x[0] in 'AEIOUaeiou', string)))


'''4) Write a function that receives a variable number of arguments and keyword arguments. The function returns a list
containing only the arguments which are dictionaries, containing minimum 2 keys and at least one string key with
minimum 3 characters.

Example:
my_function(
 {1: 2, 3: 4, 5: 6},
 {'a': 5, 'b': 7, 'c': 'e'},
 {2: 3},
 [1, 2, 3],
 {'abc': 4, 'def': 5},
 3764,
 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
 test={1: 1, 'test': True}
) will return: [{'abc': 4, 'def': 5}, {1: 1, 'test': True}]'''
def ex4(*parmas, **dict_params):
    res = []
    for param in parmas:
        if type(param) is dict and len(param.items()) > 1:
            for key in param.keys():
                if type(key) is str and len(key) > 2:
                    res.append(param)
                    break
    for d in dict_params.values():
        for item in d.items():
            if type(item[0]) is str and len(item[0]) > 2:
                res.append(d)
                break
    return res


print(ex4({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
dictionar= {'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))


'''5) Write a function with one parameter which represents a list. The function will return a new list containing all
the numbers found in the given list.
Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]'''
def ex5(param):
    res = []
    for elm in param:
        if type(elm) is dict:
            for val in elm.values():
                if type(val) is int or type(val) is float:
                    res.append(val)
        else:
            try:
                iter(elm)
                for e in elm:
                    if type(e) is int or type(e) is float:
                        res.append(e)
            except TypeError:
                if type(elm) is int or type(elm) is float:
                    res.append(elm)
    return res


print(ex5([1, "2", {"3": "a", "ceva": 12.2}, {4, 5, 6.5}, 5, 6, 3.0]))


'''6) Write a function that receives a list with integers as parameter that contains an equal number of even and odd
numbers that are in no specific order. The function should return a list of pairs (tuples of 2 elements) of numbers
(Xi, Yi) such that Xi is the i-th even number in the list and Yi is the i-th odd number
Example:
my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]) will return [(2, 1), (8, 3), (4, 5), (10, 7), (2, 9)]'''
def ex6(nums):
    even = []
    odd = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return list(zip(even, odd))


print(ex6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))


'''7) Write a function called process that receives a variable number of keyword arguments
The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following way:
If the function receives a parameter called filters, this will be a list of predicates (function receiving an argument
and returning True/False) and will retain from the generated numbers only those for which the predicates are True.
If the function receives a parameter called limit, it will return only that amount of numbers from the sequence.
If the function receives a parameter called offset, it will skip that number of entries from the beginning of the
result list.
The function will return the processed numbers.
Example:
def sum_digits(x):
    return sum(map(int, str(x)))
process(
    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
    limit=2,
    offset=2
) returns [34, 144]

Explanation:
Fibonacci sequence will be: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...
Valid numbers are: 2, 8, 34, 144, 610, 2584, 10946, 832040
After offset: 34, 144, 610, 2584, 10946, 832040
After limit: 34, 144'''
def ex7(**params):
    fib_list = [0, 1]
    while len(fib_list) < 10:
        fib_list.append(fib_list[-1] + fib_list[-2])
    print(fib_list)

    keys = params.keys()
    if "filters" in keys:
        for f in params["filters"]:
            fib_list = list(filter(f, fib_list))
    if "offset" in keys:
        fib_list = fib_list[params["offset"]:]
    if 'limit' in keys:
        fib_list = fib_list[:params["limit"]]

    return fib_list


print(ex7(offset=2, limit=1, filters=[lambda item: item > 5]))


'''8
a) Write a function called print_arguments with one parameter named function. The function will return one new
function which prints the arguments and the keyword arguments received and will return the output of the function
received as a parameter.
Example:
def multiply_by_two(x):
    return x * 2
def add_numbers(a, b):
    return a + b

augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)  # this will print: Arguments are: (10,), {} and will return 20.
augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.
'''
def print_arguments(function):
    def func(*params, **key_params):
        print(f"Arguments are: {params}, {key_params}")
        if len(key_params.items()) > 0:
            return function(*params, **key_params)
        else:
            return function(*params)
    return func


def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b

print("\na)")
augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)  # this will print: Arguments are: (3, 4), {} and will return 7.
print(f"Result: {x}")

'''
b) Write a function called multiply_output with one parameter named function. The function will return one new function 
which returns the output of the function received multiplied by 2.
Example:
def multiply_by_three(x):
    return x * 3
augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
'''
def multiply_output(function):
    def func(*params, **key_params):
        if len(key_params.items()) > 0:
            return 2 * function(*params, **key_params)
        else:
            return 2 * function(*params)
    return func


def multiply_by_three(x):
    return x * 3

print("\nb)")
augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
print(x)


'''c) Write a function called augment_function with two parameters named function and decorators. decorators will be a 
list of functions which will have the same signature as the previous functions (print_arguments, multiply_output). 
augment_function will create a new function which is augmented using all the functions in the decorators list.
Example:
def add_numbers(a, b):
    return a + b
decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 
x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))'''


def augment_function(function, decorators):
    def func(*params, **key_params):
        for dec in decorators:
            if len(key_params.items()) > 0:
                return function(*params, **key_params)
            else:
                return function(*params)
    return func


def add_numbers(a, b):
    return a + b

print("\nc)")
decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))'''
print(x)

'''
9) Write a function that receives a list of pairs of integers (tuples with 2 elements) as parameter (named pairs).
The function should return a list of dictionaries for each pair (in the same order as in the input list) that contain 
the following keys (as strings): sum (the value should be sum of the 2 numbers), prod (the value should be product of 
the two numbers), pow (the value should be the first number raised to the power of the second number) 
Example:
f9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)] )  will return [{'sum': 7, 'prod': 10, 'pow': 25}, 
{'sum': 20, 'prod': 19, 'pow': 19}, {'sum': 36, 'prod': 180, 'pow': 729000000}, {'sum': 4, 'prod': 4, 'pow': 4}] '''
def ex9(pairs):
    res = []
    for pair in pairs:
        tmp_dict = {
            'sum': pair[0] + pair[1],
            'prod': pair[0] * pair[1],
            'pow': pair[0]**pair[1]
        }
        res.append(tmp_dict)
    return res

print("ex 9)")
print(ex9([(5, 2), (19, 1), (30, 6), (2, 2)]))