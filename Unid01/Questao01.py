class Bases:
    def __init__(self):
        self.characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Caracteres para bases de 2 a 35

    def changeBase(self, num, base):
        if base < 2 or base > 35:
            print("Base inválida! Escolha uma base entre 2 e 35.")
            return

        if num == 0:
            print(f"Representação na base {base}: 0")
            return

        result = ""

        while num > 0:
            remainder = num % base
            result += self.characters[remainder]
            num //= base

        # Invertendo a string para obter a representação correta
        result = result[::-1]

        print(f"Representação na base {base}: {result}")


def main():
    b = Bases()

    num = int(input("Digite um número inteiro: "))
    base = int(input("Digite a base de destino (entre 2 e 35): "))

    b.changeBase(num, base)


if __name__ == "__main__":
    main()
