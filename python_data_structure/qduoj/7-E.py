# -*- coding: utf-8 -*-


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


p = 23333
q = 10007
n = p * q
phi_n = (p - 1) * (q - 1)

e_and_c = input().split(" ")
e, c = int(e_and_c[0]), int(e_and_c[1])
d = modinv(e, phi_n)
decrypted = pow(c, d, n)
print(decrypted)
