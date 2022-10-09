
def SumOfElements():
    value = float(input('Введите число: '))   
    sum = 0
    for i in range(1,len(str(value)) - 1):
        sum += int((value % (10**i)) / (10**(i - 1)))
    print(sum)

# SumOfElements()

def Proizvedenie():
    N = int(input('Введите число: '))
    proizvedenie = 1
    for i in range(2,N + 1):
        proizvedenie *= i
    print(proizvedenie)

# Proizvedenie()

import random
from re import X
from tempfile import tempdir
def SummaElementov1():
    N = int(input('Введите число: '))
    Spisok = []
    sum = 0
    for i in range(1, N + 1):
        Spisok.append ((1 + 1/i)**i)
    for i in range(0, N):    
        sum += Spisok[i]
    print(sum)

# SummaElementov1()


def SummaElementov2():
    N = int(input('Введите число: '))
    Spisok = []
    rez = 1
    for i in range(1, N + 1):
        Spisok.append([random.randint(- N, N)]) 
    for i in range(1, 4):   # для трех указанных в файле позиций
        x = open('file.txt', 'r')
        count = int(x.readline(i))
        rez *= int(Spisok[count])
    print(rez)

# SummaElementov2()

def Stir():
    N = int(input('Введите число: '))
    Spisok = []
    temp = 0
    for i in range(1, N + 1):
        Spisok.append([random.randint(0, N)]) 
    print(Spisok)
    for i in range(1, N + 1): 
        i = random.randint(0, N - 1)  
        temp = Spisok[i]
        Spisok[i] = Spisok[random.randint(0, N - 1)]
        Spisok[random.randint(0, N - 1)] = temp
    print(Spisok)

# Stir()