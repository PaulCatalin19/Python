# 1)
# a) Write a module named utils.py that contains one function called process_item. The function will have one parameter,
# x, and will return the least prime number greater than x. When run, the module will request an input from the user,
# convert it to a number and it will display the output of the process_item function.
def check_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, n//2, 2):
        if n % d == 0:
            return False
    return True


def process_item(x):
    x += 1
    while not check_prime(x):
        x += 1
    return x


x = int(input("number= "))
print(process_item(x))
