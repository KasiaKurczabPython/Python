# Bledy
# print(5 * (1 / 0))
# print(4 + x * 3)
# print('2' + 2)
# raise zerodivisionerror

# import sys
# try:
#     f = open("plik.txt")
#     s = f.readline()
#     i = int(s.strip())  # Usuń spacje
#     print(i)
# except OSError as err:
#     print("Błąd systemu: {0}".format(err))
# except ValueError:
#     print("Nie można dokonać konwersji.")
# except:     # PEP 8: E722 nie używaj pustego 'except'
#     print("Nieoczekiwany wyjątek:", sys.exc_info()[0])
#     raise

# try:
#     print("Dzień dobry")
# except:
#     print("Coś poszło nie tak")
# else:
#     print("Nic nie poszło źle")

# x = "dzień dobry"
# if not type(x) is int:
#     raise TypeError("Dozwolone są tylko liczby całkowite")

# while True:
#     try:
#         num1 = int(input('Podaj piewszą liczbę: '))
#         num2 = int(input('Podaj drugą liczbę: '))
#     except ValueError:
#         print("Nie wprowadziłeś liczb")
#     else:
#         print("Wynik dodawania: " (num1+num2))
#         break


# try:
#     num1 = int(input('Podaj piewszą liczbę: '))
#     num2 = int(input('Podaj drugą liczbę: '))
#     x = num1/num2
# except ZeroDivisionError:
#         x= "Dzielenie przez zero"
#         print(x)


# try:
#     num1 = int(input('Podaj piewszą liczbę: '))
#     num2 = int(input('Podaj drugą liczbę: '))
#     x = num1/num2
# except:
#     pass


# try:
#     print(a)
# except:
#     pass


# a = "123"
# b = 123
# try:
#     msg = a+b
# except IndexError:
#     msg = msg = "Nie możesz dodać int do string"
# print(msg)


# moja_lista = [1, 3, 5]
# try:
#     print(moja_lista[5])
# except IndexError:
#     print("Jesteś poza zakresem listy")


# arg = "plikXXX"
# try:
#     f = open(arg, "r")
# except IOError:
#     print("nie można otworzyć pliku", arg)
# else:
#     print(arg)
#     print(len(f.readlines()))
#     f.close()

arg = "new.py"
try:
    f = open(arg, "a")
    f.write("Dopisz cos: KKK")
    print("Sprawdz swoj plik, czy zostal zmodyfikowany")
except IOError:
    print("Nie mozna zapisac w tym pliku")
finally:
    f.close()

