'''
Returneaza true daca n este prim si false daca nu.
'''


def is_prime(n):
  # codul vostru aici

    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

assert is_prime(3) is True
assert is_prime(5) is True
assert is_prime(8) is False
assert is_prime(7) is True

'''
Returneaza produsul numerelor din lista lst.
'''
a = [1, 2, 5, 3]

def get_product(lst):
    # codul vostru aici
    s = 1

    for i in lst:
        s = s * i
    return s

'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
     while x != y:
         if x > y:
            x = x - y
         else:
             y = y - x
     return x

'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
# codul vostru aici
    for i in range(1, y + 1):
        if i <= x:
            if x % i == 0 and y % i == 0:
                z = i
    return z


def main():
# interfata de tip consola aici
    n = int(input("Numar: "))
    j=is_prime(n)
    if j == True:
        print("Numarul este prim")
    else:
        print("Numarul nu este prim")

    print("Produsul numerelor din lista este: ", get_product(a))

    p = int( input("Introduceti primul numar: ") )
    q = int( input("Introduceti al doilea numar numar: ") )

    print(f"(M1)CMMDC al celor doua numere, {p} si {q} este: ", get_cmmdc_v1(p,q) )

    p = int(input("Introduceti primul numar: "))
    q = int(input("Introduceti al doilea numar numar: "))

    print(f"(M2)CMMDC al celor doua numere, {p} si {q} este: ", get_cmmdc_v2(p,q) )

main()

