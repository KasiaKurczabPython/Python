# def add(x, y):
#     return x + y
#
#
# print(add(2, 3))
#
# def maks_lista(x):
#     n = x[0]
#     for i in x:
#         if i > n:
#             n = i
#     return n
# print(maks_lista([2,5,6,7]))

def ciag_Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return ciag_Fib(n-1) + ciag_Fib(n-2)
print(ciag_Fib(6))