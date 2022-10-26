# 1.Write a function that receives as parameters two lists a and b and returns a list of sets containing:
# (a intersected with b, a reunited with b, a - b, b - a)
def ex1(a, b):
    a = set(a)
    b = set(b)
    result = [a & b, a | b, a - b, b - a]
    return result


# 2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the
# characters in the character string and the values are the number of occurrences of that character in the given text.
# Example: For string "Ana has apples." given as a parameter the function will return the dictionary:
# {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .
def ex2(string):
    res = {}
    for char in string:
        if char not in res:
            res[char] = 1
        else:
            res[char] +=1
    return res


# 3. Compare two dictionaries without using the operator "==" returning True or False. 
# (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
def ex3():
    return


# 4. The build_xml_element function receives the following parameters: tag, content, and key-value elements given 
# as name-parameters. Build and return a string that represents the corresponding XML element. Example: 
# build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns  
# the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"
def ex4(tag, content, **key_value):
    res = "<"+ tag + " "
    for elem in key_value.items():
        print(elem)
        res = res + f'{elem[0]}=\\"{elem[1]}\\ "'
    res = res + f"> {content} </{tag}>"
    return res


# 5. The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for
# a dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows:
# (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside
# the value (not at the beginning or end) and ends with "suffix". The function will return True if the given dictionary
# matches all the rules, False otherwise.
# Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False because although the rules are
# respected for "key1" and "key2" "key3" that does not appear in the rules.
def ex5(rules, dictionary):
    for rule in rules:
        if rule[0] not in dictionary:
            return False
        if not dictionary[rule[0]].startswith(rule[1]):
            return False
        if not dictionary[rule[0]].endswith(rule[3]):
            return False
        if rule[2] not in dictionary[rule[0]][1:-1]:
            return False
    return True


# 6. Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique
# elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve this
# objective).
def ex6(items):
    count_unique = 0
    count_duplicate = 0
    tmp_set = set()
    length = 0
    for itm in items:
        tmp_set.add(itm);
        if len(tmp_set) == length:
            count_duplicate += 1
        else:
            length += 1
            count_unique += 1
    return count_unique-count_duplicate, count_duplicate


# 7. Write a function that receives a variable number of sets and returns a dictionary with the following operations
# from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b",
# where a and b are two sets, and op is the applied operator: |, &, -.
def ex7(*num_seats):
    # print("{1, 2} | {2, 3} =>", ({1, 2} | {2, 3}))
    # print("{1, 2} & {2, 3} =>", {1, 2} & {2, 3})
    # print("{1, 2} - {2, 3} =>", {1, 2} - {2, 3})
    res = {}
    for seat1 in num_seats:
        for seat2 in num_seats:
            if seat1 != seat2:
                res[str(seat1) + " | " + str(seat2)] = seat1 | seat2
                res[str(seat1) + " & " + str(seat2)] = seat1 & seat2
                res[str(seat1) + " - " + str(seat2)] = seat1 - seat2
                res[str(seat2) + " - " + str(seat1)] = seat2 - seat1
    return res


# 8. Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key
# "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the
# following way: the value of the current key is the key for the next value, until you find a loop (a key that was
# visited before). The function must return the list of objects obtained as previously described.
#
# Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
# will return ['a', '6', 'z', '2']
def ex8(mapping):
    res = []
    first = mapping['start']
    second = mapping[first]
    res.append(first)
    while first != second:
        res.append(second)
        first = str(second)
        second = mapping[first]
    return res


# 9. Write a function that receives a variable number of positional arguments and a variable number of keyword arguments
# adn will return the number of positional arguments whose values can be found among keyword arguments values.
#
# Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return 3
def ex9(*pos, **d):
    count = 0
    for value in d.values():
        if value in pos:
            count += 1
    return count


# print(ex1([1, 2, 3, 4], [2, 3, 6, 7]))
# print(ex2("Ana are multe mere"))
# print(ex3())
# print(ex4("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))
# print(ex5({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
#           {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))
# print(ex6([1, 2, 3, 4, 4, 5, 1, 3]))
# print(ex7({1, 2}, {2, 3}))
# print(ex8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
