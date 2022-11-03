import os
import sys


# 1)	Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul
# dat ca parametru.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’
def ex1(dir_address):
    extensions = set()

    for file in os.listdir(dir_address):
        if os.path.isfile(os.path.join(dir_address, file)):
            extensions.add(file.split('.')[-1])

    extensions = sorted(extensions)
    return extensions


# 2)	Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a
# fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.
def ex2(directory, file):
    f = open(file, 'w')
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            print(file)
            if file[0] == 'A':
                f.write(os.path.abspath(os.path.join(directory, file))+"\n")
    f.close()


# 3)Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului.
# Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count),
# sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu
# acea extensie. Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru.
def ex3(my_path):
    if os.path.isfile(my_path):
        data = open(my_path, 'r').read().strip()
        return data[-20:]
    else:
        extensions = {}
        for root, directories, files in os.walk(my_path):
            for file in files:
                if os.path.isfile(os.path.join(root, file)):
                    if file.split('.')[-1] not in extensions:
                        extensions[file.split('.')[-1]] = 1
                    else:
                        extensions[file.split('.')[-1]] += 1
        result = list(extensions.items())
        result.sort(key=lambda item: item[1], reverse=True)
        return result


# 4)	Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la
# linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie,deci nu va apărea în lista finală.
def ex4():
    return ex1(sys.argv[1])



# 5)	Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și returneaza o
# listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar in
# fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director. Dacă target
# nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.
def ex5(target, to_search):
    try:
        res = []
        if os.path.isfile(target):
            data = open(target, 'r').read()
            # print(f"data: {data}")
            if to_search in data:
                res.append(os.path.basename(target))
        elif os.path.isdir(target):
            for root, directories, files in os.walk(target):
                for file in files:
                    # print(f"file: {file}")
                    if os.path.isfile(os.path.join(root, file)):
                        data = open(os.path.join(root, file), 'r', encoding="utf8").read()
                        if to_search in data:
                            res.append(file)
        else:
            raise "Targe is not a file or a directory!"
        return res
    except ValueError as e:
        print(e)


# 6)	Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că
# primește un parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută
# în procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru
def ex6(target, to_search, callback):
    try:
        res = []
        if os.path.isfile(target):
            data = open(target, 'r').read()
            # print(f"data: {data}")
            if to_search in data:
                res.append(os.path.basename(target))
        elif os.path.isdir(target):
            for root, directories, files in os.walk(target):
                for file in files:
                    # print(f"file: {file}")
                    if os.path.isfile(os.path.join(root, file)):
                        data = open(os.path.join(root, file), 'r', encoding="utf8").read()
                        if to_search in data:
                            res.append(file)
        else:
            raise "Targe is not a file or a directory!"
        return res
    except ValueError as e:
        callback(e)


# 7)	Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si
# returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea
# fisierului in octeti, file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False daca
# se poate citi din/scrie in fisier.
def ex7(file_path):
    res = {}
    res["full_path"] = os.path.abspath(file_path)
    res["file_size"] = os.path.getsize(res["full_path"])
    res["file_extension"] = os.path.splitext(file_path)[-1]
    try:
        f = open(res["full_path"], "r")
        res["can_read"] = True
        f.close()
    except OSError:
        res["can_read"] = False

    try:
        f = open(res["full_path"], "w")
        res["can_write"] = True
        f.close()
    except OSError:
        res["can_write"] = False
    return res


# 8)	Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un
# director aflat pe disc. Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina
# directorului dir_path.
# Exemplu apel funcție: functie("C:\\director") va returna ["C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]
def ex8(dir_path):
    res = []
    dir_path = os.path.abspath(dir_path)
    for file in os.listdir(dir_path):
        res.append(os.path.join(dir_path, file))
    return res


# print(ex1('.'))
# ex2('.', 'fisier.txt')
# print(ex3('.'))
# print(ex4())
# print(ex5("fisier.txt", 'a'))
# print(ex6("fisier.txt", 'a', lambda e: print(f"Callback: {e}")))
# print(ex7("fisier.txt"))
print(ex8("."))
