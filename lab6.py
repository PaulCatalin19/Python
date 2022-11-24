'''1) Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence
of alpha-numeric characters.'''
import re
import os


def ex1(text):
    words = re.findall('\w+', text)
    return words


print("ex1------------------------------------------------------------------------------------------------------------")
print(ex1("Ana are multe mare!"), end="\n\n")


'''
Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns those
long-length x substrings that match the regular expression.
'''
def ex2(regex, text, x):
    return [sub_str for sub_str in re.findall(regex, text) if len(sub_str) == x]


print("ex2------------------------------------------------------------------------------------------------------------")
print(ex2('\d+', "Ana are 15 mere, 66 de nuci si 200 de pere.", 2), end="\n\n")


'''
Write a function that receives as a parameter a string of text characters and a list of regular expressions and
returns a list of strings that match on at least one regular expression given as a parameter.'''
def ex3(text, regex_list):
    res = set()
    for regex in regex_list:
        if re.search(regex, text):
            res.update(set(re.findall(regex, text)))
    return res

print("ex3------------------------------------------------------------------------------------------------------------")
print(ex3("Ana are 15 mere, 66 de nuci si 200 de pere.", ['\d+', '\w{4}', 'm.{3}']), end="\n\n")


'''Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns those
elements that have as attributes all the keys in the dictionary and values the corresponding values.
For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be those tags
whose attributes are class="url" si name="url-form" si data-id="item".'''
def ex4(pth, attrs):
    res = []
    with open(pth) as file:
        lines = [line.strip() for line in file]
        regex_list = []
        for att in attrs.items():
            regex_list.append(f"{att[0]}=\"{att[1]}\"")

        for expression in regex_list:
            lines = [line for line in lines if re.search(expression, line)]
        res = list(lines)
    return res


print("ex4------------------------------------------------------------------------------------------------------------")
print(*ex4(r'D:\private\Python\Python-course\Python course\lab6.xml',
      attrs={"class": "url", "name": "url-form", "data-id": "item"}), sep="\n", end="\n\n")


'''Write another variant of the function from the previous exercise that returns those elements that have at least one 
attribute that corresponds to a key-value pair in the dictionary.'''
def ex5(pth, attrs):
    res = set()
    with open(pth) as file:
        lines = [line.strip() for line in file]
        regex_list = []
        for att in attrs.items():
            regex_list.append(f"{att[0]}=\"{att[1]}\"")

        for expression in regex_list:
            res.update([line for line in lines if re.search(expression, line)])
    return list(res)


print("ex5------------------------------------------------------------------------------------------------------------")
print(*ex5(r'D:\private\Python\Python-course\Python course\lab6.xml',
      attrs={"class": "url", "name": "url-form", "data-id": "item"}), sep="\n", end="\n\n")


'''Write a function that, for a text given as a parameter, censures words that begin and end with vowels. Censorship
means replacing characters from odd positions with *.'''
def censor(match):
    text = str(match.group(0))
    # print("text"+text)
    res = ""
    for index in range(0, len(text)):
        if index % 2 == 0:
            res = res + text[index]
        else:
            res = res +"*"
    return res


def ex6(text):
    return re.sub(r'\b[aeiouAEIOU]\w*[aeiou]', censor, text)


print("ex6------------------------------------------------------------------------------------------------------------")
print(ex6("Anastasia are multe mere"), end="\n\n")


'''Verify using a regular expression whether a string is a valid CNP.'''
def ex7(cnp):
    # print(f"len: {len(cnp)}")
    reg = r"[1-8]([0-9]{2})(0[1-9]|1[0-2])(0[[1-9]|1[0-9]|2[0-9]|3[0-1])\d{6}"
    if not re.search(reg, cnp):
        return False
    return True


print("ex7)------------------------------------------------------------------------------------------------------------")
print(ex7("1591125236421"), end="\n\n")


'''Write a function that recursively scrolls a directory and displays those files whose name matches a regular 
expression given as a parameter or contains a string that matches the same expression. Files that satisfy both 
conditions will be prefixed with ">>"'''
def ex8(dir_path, regex):
    res = set()
    for root, directories, files in os.walk(dir_path):
        for file in files:
            if os.path.isfile(os.path.join(root, file)):
                with open(os.path.join(root, file)) as opened_file:
                    data = opened_file.read()
                    if re.search(regex, data):
                        res.update([file])
                if re.search(regex, file):
                    res.update([file])
    return res


print("ex8)------------------------------------------------------------------------------------------------------------")
print(ex8(r'D:\private', r'\.txt'), end="\n\n")
