# print("Hello World")
# x = 5
# y = 15
# if(x>3) or (y%2 == 0):
#     print("Żaden warunek nie jest spełniony")
# if(x<=3) and (y%2 <> 0):
#     print("Co najmniej jeden z warunków jest spełniony")

# x = False
# if not x:
#     print("warunek spełniony")
# else:
#     print("warunek niespełniony")

# niepusta_wartosc = 0 or 0.0 or "" or [] or "test" or [123]
# print(niepusta_wartosc)
# wszystko niepuste i zerowe jest FALSE
# wszystko inne jest TRUE
# Python poruszając sie od początku od lewej do prawej ewaluuje wartości i przypisze test

# kazda_wartosc = "test" and [123]
# print(kazda_wartosc)

# operator trojskladnikowy if-else

# nice = True
# personality = ("wredny", "miły") [nice]
# skojarzyc z krotką, pierwsza pozycja to 0 czyli False, druga pozycja to 1 czyli True
# gdy bedzie wiecej elementow w krotce, to one sie nie wyciagna

# # Petla For
# string = "Python"
# # Pętla:
# for litera in string: # tutaj mozna ograniczyc np. string[2]
#     print('litera:', litera)

# Gdyby nie było pętli:
# litera = string[0]
# print('litera:', litera)
# litera = string[1]
# print('litera:', litera)
# litera = string[2]
# print('litera:', litera)
# litera = string[3]
# print('litera:', litera)
# litera = string[4]
# print('litera:', litera)
# litera = string[5]
# print('litera:', litera)

# lista = ['Julia', 'Janusz', 'Karolina', 'Kasia']
# lista.sort()
# kobiety = 0
# for imie in lista:
#     if imie[-1] = 'a':
#         kobiety = 1
# print(kobiety)


# for num in range(1, 20):
#     if not num % 2:  # num % 2 == 0
#         print('Kolejna liczba parzysta:', num)
#         continue
#     print('Kolejna liczba:', num)


# Zadanie
# Napisz program, który policzy największy wspólny dzielnik dwóch liczb podanych przez użytkownika
# W tym celu użyj operatora % oraz pętli for

# x = int(nput("Podaj liczbę: "))
# y = int(input("Podaj liczbę: "))

# x = 100
# y = 20
# if x < y:
#     z = x
# else:
#     z = y
#
# for i in (z, 0, -1):
#     if i % 2 == 0 and i % 2 ==  0:
#         continue
#     print("Wspolny dzielnik: ", i)
#     break

# print("Hello World")
# input("Tell me your name")

# x = 15
# y = 8
# if x>3 and y%2 == 0:
#     print("warunek jest spelniony")
# else:
#     print("Zaden warunek nie jest spelniony")


# def simple_function():
#     print('Hello world!')
#     print('Wikipedia')
#
#
# simple_function()

# def my_function():
#     return 3+3
#
#
# print(my_function())

# def add(x, y):
#     return x + y
#
#
# print(add(2, 3))

# def my_function():
#     """Dokumentacja funkcji"""
# help(my_function())

# def fibbonaci_numbers(n):
#     # for i (2,12,1)
#     #     i = i + (i-1)
#     wynik = []
#     a, b = 0, 1
#     # while a < n:
#     while len(wynik) < n:
#         wynik.append(a)
#         a, b = b, a+b
#     return(wynik)
#
# x = fibbonaci_numbers(20)
# print(x)
# print(fibbonaci_numbers.__doc__)

# def dlugosc_lancucha_znakow(x):
#     i = 0
#     for z in x:
#         i += 1
#     return i
#
# print(dlugosc_lancucha_znakow("kot"))

# def suma_elementow_listy(x):
#     i = 0
#     for z in x:
#         i += 1
#     return i
# print(suma_elementow_listy([1,2,3]))

# def iloczyn_lista(x):
#     n = x[0]
#     for i in x[1:]:
#         n *= i
#     return n
# print(iloczyn_lista([2,5,6,7]))

# def maksimum(lista):
#     wartosc_maksymalna = lista.pop()
#     for wartosc in lista:
#         if wartosc > wartosc_maksymalna:
#             wartosc_maksymalna = wartosc
#         return wartosc_maksymalna
# print(maksimum([1,5,50,1]))

# element = "google.com"
# def count(element):
#     dict = {}
#     for i in element:
#         if i in dict.keys():
#             dict[i]+=1
#         else:
#             dict[i]= 1
#     return dict
# print(count(element))

# Przykładowa_lista = ['abc', 'xyz', 'aba', '1221']
#
# def licznik(lista):
#     n = 0
#     for x in lista:
#         if len(x)>=2 and x[0] == x[-1]:
#             n += 1
#     return n
# print(licznik(Przykładowa_lista))

# Przykładowa_lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1, 0)]
# def zwrot_elementu(x):
#     return x[-1]
# Przykładowa_lista.sort(key=zwrot_elementu)
# print(Przykładowa_lista)

# def silnia(n):
#     if n == 1:
#         return 1
#     else:
#         return n * silnia(n-1)
# print(silnia(5))

def ciag_Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return ciag_Fib(n-1) + ciag_Fib(n-2)
print(ciag_Fib(6))

