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

# Petla For
string = "Python"
# Pętla:
for litera in string: # tutaj mozna ograniczyc np. string[2]
    print('litera:', litera)

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

x = int(nput("Podaj liczbę: "))
y = int(input("Podaj liczbę: "))

if x < y:
    z = x
else:
    z = y

for i in (z, 0, -1):
    if x % i == 0 and y % i == 0:
        print("Wspolny dzielnik: ", i)
        break



