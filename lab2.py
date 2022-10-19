import collections


def ex1():
    n = int(input("n= "))
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        res = [0, 1]
        for i in range(2, n):
            res.append(res[-1]+res[-2])
        return res


def ex2(list_num):
    res = []
    for num in list_num:
        if num == 2:
            res.append(2)
        if num % 2 != 0 and num > 2:
            res.append(num)
            for div in range(3, int(num**1/2)+1, 2):
                if num % div == 0:
                    res.pop()
    return res


def ex3(list_a, list_b):
    inter = [num for num in list_a if num in list_b]
    union = list_a + [num for num in list_b if num not in list_a]
    sub_1 = [num for num in list_a if num not in list_b]
    sub_2 = [num for num in list_b if num not in list_a]

    return [inter, union, sub_1, sub_2]


def ex4(notes, moves, start):
    res = [notes[start]]
    pos = start
    for i in moves:
        pos = (pos+i) % len(notes)
        res.append(notes[pos])
    return res


def ex5(matrix):
    n = len(matrix)
    print(n)
    for i in range(n):
        for j in range(n):
            if j < i:
                matrix[i][j] = 0
    return matrix


def ex6(x, *lists):
    # x = lists[-1]
    d = collections.defaultdict(int)
    for l in lists:
        for elm in l:
            d[elm] += 1

    res = [item[0] for item in d.items() if item[1] == x]
    return res


def ex7(list_of_numbers):
    max_num = 0
    count = 0
    for num in list_of_numbers:
        rev_num = int(str(num)[::-1])
        if num == rev_num:
            count += 1
            if max_num < num:
                max_num = num
    return count, max_num


def ex8(strings, flag=True, x=1):
    res = []
    for str_elm in strings:
        str_sol = []
        for character in str_elm:
            if (ord(character) % x == 0 and flag) or (ord(character) % x != 0 and not flag):
                str_sol.append(character)
        res.append(str_sol)
    return res


def ex9(matrix):
    result = []
    lines = len(matrix)
    cols = len(matrix[0])
    for c in range(cols):
        max_col = matrix[0][c]
        for l in range(1, lines):
            if matrix[l][c] <= max_col:
                result.append((l, c))
            else:
                max_col = matrix[l][c]
    return result


def ex10(*lists):
    result = list(zip(*lists))
    return result


def ex11(list_of_tuples):
    list_of_tuples.sort(key=lambda tpl: tpl[1][2])
    return list_of_tuples


def ex12(words):
    words_dict = dict()
    for word in words:
        if word[-2:] not in words_dict:
            words_dict[word[-2:]] = []
        words_dict[word[-2:]].append(word)

    return list(words_dict.values())


# print(ex1())
# print(ex2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 23, 25]))
# print(ex3([1, 2, 3, 5], [0, 2, 4, 5]))
# print(ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
# print(ex5([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
# print(ex6(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
# print(ex7([123, 521, 112396723, 121, 12, 111, 373]))
# print(ex8(["test", "hello", "lab002"], False, 2))
# print(ex9(
#     [[1, 2, 3, 2, 1, 1],
#     [2, 4, 4, 3, 7, 2],
#     [5, 5, 2, 5, 6, 4],
#     [6, 6, 7, 6, 7, 5]]
# ))
# print(ex10([1, 2, 3], [5, 6, 7, 6], ["a", "b", "c"]))
# print(ex11([('abc', 'bcd'), ('abc', 'zza')]))
print(ex12(['ana', 'banana', 'carte', 'arme', 'parte']))
