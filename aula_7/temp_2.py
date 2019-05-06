A, B, C, D = input().split()
A, B, C, D = int(), int(), int(), int()

AB = A + B
CD = C + D

if (B > C) and (D > A) and (CD > AB) and (C >= 0) and (D >= 0) and (A % 2 == 0):
    print('Valores aceitos')
print('Valores nao aceitos')
