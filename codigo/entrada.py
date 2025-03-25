class Entrada:

    def __init__(self,string) -> None:

        self.__entrada = self.sanitiza_entrada(string)


    ans= .2 + .1 = 0.3
    ans = 2*1
    ans = 2 - 1
    ans = 2 / 1
    ans = 2 % 1

    def sanitiza_entrada(self, string: str):
        entrada = string.strip()


        0123456789.+-*/^<>=()%!zxcvbnmasdfghjklqwerftyuiopZXCVBNMASDFGHJKLQWERETYUIOP

    def string_para_lista_de_inteiros(self, string: str) -> list:
        return [int(char) for char in string]

    def is_zero(self, vetor: list) -> bool:
        return len(vetor) == 1 and vetor[0] == 0

    def retorna_expoente_depois_do_separador(self, vetor: list) -> None:
        contador = 0

        for var in vetor:
            if var != 0:
                return contador
            else:
                contador -= 1

    def converte_entrada_para_mantissa(self, numero: str) -> None:

        if numero is None or numero == "0.0":
            self.mantissa.append(0)
            self.tamanho += 1
        else:
            vetor = numero.split(".")
            antes,depois = vetor[0],vetor[1]

            antes = self.string_para_lista_de_inteiros(antes)
            depois = self.string_para_lista_de_inteiros(depois)

            if self.is_zero(antes):
                self.expoente = (
                self.retorna_expoente_depois_do_separador(depois)
                )
                depois = depois[ -self.expoente:]
            else:
                self.expoente = len(antes)

            self.tamanho += len(antes) + len(depois)
            self.mantissa = antes + depois