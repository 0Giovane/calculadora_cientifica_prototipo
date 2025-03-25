from constantes import (COMPRIMENTO_DA_MANTISSA,
                        BASE_DECIMAL)


class Numero:

    def __init__(self,numero: str = None,
                      expoente: int = 0,
                      base: int = BASE_DECIMAL,
                      mantissa: list = [],
                      tamanho: int = 0) -> None:

        self.__mantissa = mantissa
        self.__tamanho = tamanho
        self.__expoente = expoente
        self.__base = base

        self.converte_entrada_para_mantissa(numero)

    # ===============================================================

    @property
    def mantissa(self):
        return self.__mantissa

    @mantissa.setter
    def mantissa(self, mantissa):
        self.__mantissa = mantissa

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, valor):
        self.__tamanho = valor

    @property
    def expoente(self):
        return self.__expoente

    @expoente.setter
    def expoente(self, valor):
        self.__expoente = valor

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, valor):
        self.__base = valor

    # ===============================================================

    def __getitem__(self, posicao) -> int:
        return self.mantissa[posicao]

    def __setitem__(self, posicao, valor) -> None:
        self.mantissa[posicao] = valor

    def __add__(self, outro):
        if self.expoente > outro.expoente:
            maior = self.expoente
            menor = outro.expoente
        else:
            maior = outro.expoente
            menor = self.expoente

        expoente = maior
        diferenca = maior - menor

        if maior == self.expoente:
            mantissa_1 = self.mantissa.copy()
            mantissa_2 = outro.deslocar_a_direita(diferenca)
        else:
            mantissa_1 = outro.mantissa.copy()
            mantissa_2 = self.deslocar_a_direita(diferenca)

        if len(mantissa_1) > len(mantissa_2):
            mantissa_maior = mantissa_1
            mantissa_menor = mantissa_2
        else:
            mantissa_maior = mantissa_2
            mantissa_menor = mantissa_1

        tamanho_maior = tamanho = len(mantissa_maior)
        tamanho_menor = len(mantissa_menor)

        for var in range(tamanho_maior):
            if var < tamanho_menor:
                mantissa_maior[var] += mantissa_menor[var]
            else:
                return mantissa_maior,tamanho,expoente
        return mantissa_maior, tamanho, expoente



    # ===============================================================

    def deslocar_a_direita(self, n: int) -> list:
        mantissa = self.mantissa.copy()
        tamanho = self.tamanho
        for var in range(n):
            mantissa.insert(0,0)
            tamanho += 1
            if tamanho > COMPRIMENTO_DA_MANTISSA:
                mantissa.pop()

        return mantissa




