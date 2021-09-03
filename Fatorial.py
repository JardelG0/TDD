"""Lista1_Q14
Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!"""


def fator(valor):
    fatorial = 1
    for i in range(1, valor+1):
        fatorial *= i
    return fatorial


def soma(n):
    s = 1
    for i in range(1, n + 1):
        s += 1 / fator(i)
    return s


def main():
    while True:
        try:
            n = int(input(""))
            if n >= 0:
                print("Resultado:",round(soma(n), 2))
                break
            else:
                print("Número negativo!")
        except:
            print("Número inválido!")


if __name__ == "__main__":
    main()
