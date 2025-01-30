import math

def f(x):
    return math.sqrt(1 - x**2)

def um_terco_simpson(a, b, n, f):
    deltax = (b-a)/n

    soma1=0
    soma2=0
    soma3=0
    for i in range(n):
        x=a+deltax*i
        if (i==0 or i==n):
            soma1 = (soma1 + f(x))
        elif (i%2==0):
            soma2 = (soma2 + 2*f(x))
        else:
            soma3 = (soma3 + 4*f(x))
    soma = (soma1 + soma2 + soma3)*(deltax/3)
    return abs(soma)

def tresoitavos_simpson(a, b, n, f):
    deltax = (b-a)/n

    soma1=0
    soma2=0
    soma3=0
    for i in range(n):
        x = a+deltax*i
        if (i==0 or i==n):
            soma1 = (soma1 + f(x))
        elif (i%3==0):
            soma2 = (soma2 + 2*(f(x)))
        else:
            soma3 = (soma3 + 3*f(x))
    soma = (soma1 + soma2 + soma3)*(deltax*3/8)
    return abs(soma)

def erro(exato, aproximado):
    return ((exato - aproximado)/exato)*100
#Main
area_terco_simpson = um_terco_simpson(-1, 1, 8, f)
erro_1_3 = erro(math.pi/2, area_terco_simpson)
area_3oitavos_simpson = tresoitavos_simpson(-1, 1, 9, f)
erro_3_8 = erro(math.pi/2, area_3oitavos_simpson)

print("[Valor exato]")
print("----------------------------------")
print(f"Área: {(math.pi/2):.4f}")
print("----------------------------------")

print("\n[Método 1/3 de Simpson]")
print("----------------------------------")
print(f"Área: {area_terco_simpson:.4f}")
print(f"Erro percentual: {erro_1_3:.2f} %")
print("----------------------------------")

print("\n[Método 3/8 de Simpson]")
print("----------------------------------")
print(f"Área: {area_3oitavos_simpson:.4f}")
print(f"Erro percentual: {erro_3_8:.2f} %")
print("----------------------------------")
