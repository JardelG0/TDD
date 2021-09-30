from random import randint

def cart_gabarito():
    c_gabarito = []
    alternativas = "A", "B", "C", "D", "E"
    respost = []
    for i in range(30):
        respost.append(randint(0, 4))
    for j in range(30):
        c_gabarito.append(alternativas[respost[j]])
    return c_gabarito


def alun_gabarito(alun):
    alunos = []
    for i in range(alun):
        v_temp = []
        for j in range(30): 
            v_temp.append(str(input(f'{j + 1}° Alternativa >_')).upper())
        alunos.append(v_temp)
    return alunos


def correção(gabarito_verif, gabarito_alun, qtd_alun):
    result_alun = []
    for i in range(qtd_alun):
        corret = 0
        for j in range(30):
            if gabarito_alun[i][j] == gabarito_verif[j]:
                corret += 1
        result_alun.append(corret)
    return result_alun


def main():
    c_gab = cart_gabarito()
    qtd_alun = int(input("Quantidade de alunos: "))
    a_gab = alun_gabarito(qtd_alun)
    acertos = correção(c_gab, a_gab, qtd_alun)
    for i in range(qtd_alun):
        print(f'O aluno {i+1} tem {acertos[i]} acertos!')


if __name__ == "__main__":
    main()
