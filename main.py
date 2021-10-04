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
    while True:
        print("1. Verificare primalitate. ")
        print("2. Produsul numerelor unei liste. ")
        print("3. CMMDC Metoda 1. ")
        print("4. CMMDC Metoda 2. ")
        print("x. Iesire din program. ")
        optiune = input("Alege optiunea: ")
        if optiune == '1':
            n = int(input("Numar: "))
            j=is_prime(n)
            if j == True:
                print("Numarul este prim")
            else:
                print("Numarul nu este prim")

        elif optiune == '2':
            numere_str = input("Introduceti numerele separate prin spatiu: ")
            numere_str_lst = numere_str.split(' ')
            numere_int_lst = []
            for nr_str in numere_str_lst:
                numere_int_lst.append(int(nr_str))
            produsul_numerelor = get_product(numere_int_lst)
            print("Produsul numerelor din lista este: ", produsul_numerelor)
        elif optiune == '3':
            p = int( input("Introduceti primul numar: ") )
            q = int( input("Introduceti al doilea numar numar: ") )

            print(f"(M1)CMMDC al celor doua numere, {p} si {q} este: ", get_cmmdc_v1(p,q) )
        elif optiune == '4':
            p = int(input("Introduceti primul numar: "))
            q = int(input("Introduceti al doilea numar numar: "))

            print(f"(M2)CMMDC al celor doua numere, {p} si {q} este: ", get_cmmdc_v2(p,q) )
        elif optiune == 'x':
            break
        else:
            print("Optiune invlaida! Reincercati!")

main()

