import numpy as np

#Valores iniciais
a = 0 #Inicio do intervalo
b = 1200 #Fim do intervalo
h = 80 #Passo do intervalo
n = 15 #Número de partições
x = np.arange(a, b+h, h) #Valores de X 
x =      [0,  80,   160,  240,320, 400, 480, 560, 640, 720, 800, 880, 960, 1040, 1120, 1200]
y_cima = [0, -0.4, -0.8, -1.5, -2, 480, 480, 480, 260, 230, 210, 200, 185,  210,  190, 0] #Valores de y(função de cima)
y_baixo = [0, -80, -160, -305, -330, -245, -250, -325, -480, -600, -640, -650, -410, -380, -250, -240] #Valores de y(função de baixo)

def plotar_grafico():
    import matplotlib.pyplot as plt
    plt.plot(x, y_cima, color='blue', marker='', linewidth=1.0)
    plt.plot(x, y_baixo, color='green', marker='', linewidth=1.0)
    plt.grid()
    plt.show()

def ponto_central(a, b, n, y):
    deltax=((b-a)/n)

    soma=0
    for i in range(n):
        soma += y[i]*deltax
    return abs(soma)

def tresoitavos_simpson(a, b, n, y):
    deltax = (b-a)/n

    soma1=0
    soma2=0
    soma3=0
    for i in range(n):
        if (i==0 or i==n):
            soma1 = (soma1 + y[i])
        elif (i%3==0):
            soma2 = (soma2 + 2*y[i])
        else:
            soma3 = (soma3 + 3*y[i])
    soma = (soma1 + soma2 + soma3)*(deltax*3/8)
    return abs(soma)

def erro(exato, aproximado):
    return ((exato - aproximado)/exato)*100

#Main
area_exata = 695662
area_ponto_central = (ponto_central(a, b, n, y_cima) + ponto_central(a, b, n, y_baixo))
erro_ponto_central = erro(area_exata, area_ponto_central)
area_3oitavos = (tresoitavos_simpson(a, b, n, y_cima) + tresoitavos_simpson(a, b, n, y_baixo))
erro_3oitavos = erro(area_exata, area_3oitavos)

print("[Área Exata]")
print("----------------------------------")
print(f"Área: {area_exata} Km²")
print("----------------------------------")

print("\n[Método do Ponto Central Composto]")
print("----------------------------------")
print(f"Área Total: {area_ponto_central} Km²")
print(f"Erro percentual: {erro_ponto_central:.2f} %")
print("----------------------------------")

print("\n[Método 3/8 de Simpson]")
print("----------------------------------")
print(f"Área Total: {area_3oitavos} Km²")
print(f"Erro percentual: {erro_3oitavos:.2f} %")
print("----------------------------------")

#plotar_grafico()