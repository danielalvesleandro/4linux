import math


# exercicio de revisão
# escrever uma função que recebe 
# dois pontos(ou vetores)
# e retorna a soma vetorial
#ponto = (0, 0) #coordenadas

A = 2, 1
B = 3, 5

def soma_vetorial(p, q):
    return p[0] + q[0], p[1] + q[1]
    
print(soma_vetorial(A, B))


exit()

def area_do_circulo(raio, precisao_do_pi=50):
    return raio * math.pi

print(area_do_circulo(1))
print(area_do_circulo(5))
print(area_do_circulo(raio=10, precisao_do_pi=20))