def main():
    class creditCard:
        def __init__(self, numero, titular, valid_mes, valid_ano, cod_segurança, valor_min_pagar=0, senha =None, fatura_a_pagar=0, status = "bloqueado", limite_de_compras=100):
            self.__numero = numero
            self.__titular = titular
            self.__validade = [valid_mes, valid_ano]
            self.__cod_segurança = cod_segurança
            self.__valor_min_a_pagar = valor_min_pagar
            self.__senha = senha
            self.__fatura_a_pagar = fatura_a_pagar
            self.__status = status
            self.__limite_de_compras = limite_de_compras
        
        @property
        def numero(self):
            return self.__numero
        @property
        def titular(self):
            return self.titular
        @property
        def fatura_a_pagar(self):
            return self.__fatura_a_pagar
        @property
        def valor_min_a_pagar(self):
            return self.__valor_min_a_pagar

        def desbloquear(self):
            if self.__status != "liberado":
                self.__status = "liberado"
                print("Cartão desbloqueado!")
            else:
                print("Cartão já está desbloqueado!")
        def bloquear(self):
            if self.__status != "bloqueado":
                self.__status = "bloqueado"
                print("Cartão bloqueado!")
            else:
                print("Cartão já está bloqueado!")
        def mudar_senha(self, cod_segur, new_key):
            if type(cod_segur) == int and cod_segur == self.__cod_segurança:
                if new_key != self.__senha and type(new_key) == int:
                    self.__senha = new_key
                    print("Senha alterada com sucesso!")
                else:
                    print("Tente outra senha e utilize apenas números!")
            else:
                print("Erro! código de segurança incorreto")
        def comprar(self, compra, mes_v, ano_v, passw):
            if compra < self.__limite_de_compras:
                if self.__status == "liberado":
                    if ano_v == self.__validade[1]:
                        if mes_v < self.__validade[0]:
                            if passw == self.__senha:
                                self.__limite_de_compras -= compra
                                self.__fatura_a_pagar += compra
                                self.__valor_min_a_pagar += (30 * compra) / 100
                                print("Compra realizada com sucesso!")
                            else:
                                print("Senha incorreta!")
                        else:
                            print("Compra não realizada! Cartão vencido")
                    elif ano_v < self.__validade[1]:
                            if passw == self.__senha:
                                self.__limite_de_compras -= compra
                                self.__fatura_a_pagar += compra
                                self.__valor_min_a_pagar += (30 * compra) / 100
                                print("Compra realizada com sucesso!")
                            else:
                                print("Senha incorreta!")
                    else:
                        print("Compra não realizada! Cartão vencido")
                else:
                    print("Compra não realizada! Cartão está bloqueado")
            else:
                print("Compra não realizada! Limite ultrapassado")
        def pagar_fatura(self, valor):
            if float(valor) >= self.__valor_min_a_pagar:
                if float(valor) <= self.__fatura_a_pagar:
                    self.__fatura_a_pagar -= valor
                    self.__limite_de_compras += valor
                    print("Pagamento realizado com sucesso!")
                else:
                    print("O pagamento excede o valor da fatura!")
            else:
                print("Pagamento abaixo do valor mínimo!")
        def __str__(self):
            return "Número do Cartão :{}\nNome do titular: {}\nValor da Fatura: {}\nValor Mínimo a Pagar: {}"\
                .format(self.__numero, self.__titular, self.__fatura_a_pagar, self.__valor_min_a_pagar)

    card_c = creditCard(286, "José", 2, 2022, 133)
    card_c.desbloquear()
    card_c.desbloquear()
    card_c.mudar_senha(133, 2234)
    card_c.comprar(120, 1, 2022, 2234)
    print(card_c,"\n")

    card_c2 = creditCard(334, "Maria", 11, 2021, 343)
    card_c2.bloquear()
    card_c2.desbloquear()
    card_c2.comprar(99, 6, 2022, 2234)
    print(card_c2,"\n")

    card_c3 = creditCard(873, "Joãozinho", 8, 2023, 231)
    card_c3.comprar(50, 12, 2022, 231)
    card_c3.desbloquear()
    card_c3.mudar_senha(231, 5463)
    card_c3.comprar(50, 12, 2022, 5463)
    card_c3.pagar_fatura(16)
    print(card_c3,"\n")

    card_c4 = creditCard(132, "Eduarda", 5, 2021, 132)
    card_c4.desbloquear()
    card_c4.mudar_senha(132, 3334)
    card_c4.comprar(101, 7, 2020, 3334)
    card_c4.comprar(98, 7, 2020, 3334)
    card_c4.pagar_fatura(98)
    card_c4.bloquear()
    print(card_c4)



if __name__ == "__main__":
    main()
