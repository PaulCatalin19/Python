import collections

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def ex1():
    numbers = [int(x) for x in input().split()]
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
    print(result)

def ex2():
    str1 = input("string = ").lower()
    # print(str1)
    v_no = 0
    for c in str1:
        if c in "aeiou":
            v_no = v_no + 1
    print(f"vowels number: {v_no}")


def ex3():
    str1 = input("string 1 = ")
    str2 = input("string 2 = ")
    occur = str2.count(str1)
    print(f"number of occurrences {occur}")


def ex4():
    string = input("string = ")
    sol = [string[0].lower()]
    for c in string[1:]:
        if c in "QWERTYUIOPASDFGHJKLZXCVBNM":
            sol.append('_')
        sol.append(c.lower())
    sol = ''.join(sol)
    print(sol)


def ex5(matrix, i, j, n, m):
    sol = ""
    if i > n or j > m:
        return ''
    for k in range(j, m):
        sol += str(matrix[i][k])
    for k in range(i+1, n):
        sol += str(matrix[k][m-1])
    if n-1 != i:
        for k in range(m-2, j-1, -1):
            sol += str(matrix[n-1][k])
    if m-1 != j:
        for k in range(n-2, i, -1):
            sol += str(matrix[k][j])
    return sol + ex5(matrix, i+1, i+1, n-1, m-1)


def ex6():
    number = input("number= ")
    rev_number = number[::-1]
    print(number, rev_number)
    if number == rev_number:
        print("Palindrome")
    else:
        print("Not palindrome")


def ex7():
    string = input("string= ")
    for s in string.split():
        if s.isnumeric():
            print(s);
            break


def ex8():
    number = int(input("number= "))
    binary = bin(number)
    print(number)
    print(binary)
    print(binary.count("1"))


def ex9():
    string = input("string= ").lower()
    d = collections.defaultdict(int)
    for c in string:
        if c.isalpha():
            d[c] += 1
    res = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(res)
    print(res[0])


def ex10():
    words = input("string= ").split(' ')
    print(words)
    print(f"Number of words: {len(words)}")


ex1()
# ex2()
# ex3()
# ex4()
# print(ex5([
#     'firs',
#     'n_lt',
#     'oba_',
#     'htyp'
# ], 0, 0, 4, 4))
# ex6()
# ex7()
# ex8()
# ex9()
# ex10()

