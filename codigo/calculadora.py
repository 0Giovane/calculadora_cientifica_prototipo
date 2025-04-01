from importlib import reload

import funcoes as f
from constantes import FUNCAO_RESPOSTA,NOME_FUNCAO_RESPOSTA,PROPRIEDADES_FUNCAO_RESPOSTA

class Funcoes:
    def __init__(self):
        self.__posicao_livre = 0
        self.__funcoes_props = []
        self.__funcoes_nomes = {}
        self.__indice = -1
        self.atualiza_nomes()


    #================================================================
    @property
    def posicao_livre(self):
        return self.__posicao_livre

    @posicao_livre.setter
    def posicao_livre(self, valor):
        self.__posicao_livre = valor

    @property
    def funcoes_props(self):
        return self.__funcoes_props

    @funcoes_props.setter
    def funcoes_props(self, valor):
        self.__funcoes_props = valor

    @property
    def funcoes_nomes(self):
        return self.__funcoes_nomes

    @funcoes_nomes.setter
    def funcoes_nomes(self, valor):
        self.__funcoes_nomes = valor

    @property
    def indice(self):
        return self.__indice

    @indice.setter
    def indice(self, valor):
        self.__indice = valor

    # ================================================================

    def atualiza_nomes(self):
        with open("nomes_das_funcoes.txt") as arquivo:
            for linha in arquivo.readlines():
                entrada = linha.strip()
                valor = entrada.split(",")
                self.indice += 1
                self.funcoes_props.append(list(map(int,[valor[1],valor[2]])))
                self.funcoes_nomes[valor[0]] = self.indice
            if len(self.funcoes_props) > 0:
                self.posicao_livre = self.funcoes_props[-1][1]

    def nova_funcao(self,nome_da_funcao: str = "resp",
                    resultado: str = "0",
                    nome_fantasia: str = "resp") -> None:

        with open("funcoes.py","a",encoding="utf-8") as arquivo:
            posicao_comeco = self.posicao_livre

            string = (f"def {nome_da_funcao}():\n"+
                      f"\treturn {resultado}\n"
                      )

            arquivo.write(string)

            self.posicao_livre = posicao_final = posicao_comeco + len(string)
            self.indice += 1

            self.funcoes_props.append([posicao_comeco,posicao_final])
            self.funcoes_nomes[nome_fantasia] = self.indice
            with open("nomes_das_funcoes.txt","a") as nomes:
                nomes.write(nome_fantasia + f",{posicao_comeco},{posicao_final}\n")

    def editar_funcao(self,nome_da_funcao: str,
                      resultado: str = "0") -> None:
        original = ""
        with open("funcoes.py","r",encoding="utf-8") as leitor:
            original = leitor.read()

        with open("funcoes.py","w",encoding="utf-8") as editor:
            indice = self.funcoes_nomes[nome_da_funcao]

            posicao_comeco = self.funcoes_props[indice][0]
            posicao_final = self.funcoes_props[indice][1]

            string =   (f"def {nome_da_funcao}():\n" +
                        f"\treturn {resultado}\n"
                       )

            original = (original[:posicao_comeco]    +
                        string                       +
                        original[posicao_final:]
                        )

            editor.write(original)

            posicao_final = posicao_comeco + len(string)

            self.corrige_posicoes(indice,posicao_final)

    def corrige_posicoes(self,indice,posicao_final):

            self.funcoes_props[indice][1] = posicao_final

            with open("nomes_das_funcoes.txt") as leitura:
                propriedades = [linha.strip().split(",") for linha in leitura.readlines()]
                with open("nomes_das_funcoes.txt","w") as escritor:
                    propriedades[indice][2] = str(posicao_final)

                    for posicao in range(indice + 1, len(self.funcoes_props)):
                        comprimento = self.funcoes_props[posicao][1] - self.funcoes_props[posicao][0]
                        self.funcoes_props[posicao][0] = posicao_final
                        propriedades[posicao][1] = str(posicao_final)
                        posicao_final = posicao_final + comprimento
                        self.funcoes_props[posicao][1] = posicao_final
                        propriedades[posicao][2] = str(posicao_final)
                    string_saida = ""
                    for linha in propriedades:
                        for elemento in linha:
                            string_saida += elemento + ","
                        string_saida = string_saida[:len(string_saida) - 1]
                        string_saida += "\n"
                    escritor.write(string_saida)

    def tratamento_para_nome(self,nome):
        return f"_{nome}"

    def tratamento_para_retorno(self,retorno):
        string = retorno
        for nome in self.funcoes_nomes:
            fragemento_do_retorno = retorno
            dif = 0
            dif_nome = len(nome) + 3
            while nome in fragemento_do_retorno:
                posicao_inicial = fragemento_do_retorno.find(nome) + dif
                posicao_final = posicao_inicial + len(nome)
                fragemento_do_retorno = fragemento_do_retorno[posicao_final:]
                dif = dif_nome
                string = string[:posicao_inicial] + "_" + f"{nome}" + "()" + string[posicao_final:]
        return string

    def fabrica_funcoes(self,nome_fantasia,resultado):

        nome_funcao = self.tratamento_para_nome(nome_fantasia)
        resp = self.tratamento_para_retorno(resultado)

        if nome_fantasia in self.funcoes_nomes:
            self.editar_funcao(nome_funcao,resp)
        else:
            self.nova_funcao(nome_funcao,resp,nome_fantasia)

        self.editar_funcao("resp",f"{nome_funcao}()")

    def reiniciar(self):

        with open("funcoes.py", "w") as editor:

            editor.write(FUNCAO_RESPOSTA)

            self.posicao_livre = len(FUNCAO_RESPOSTA)

            self.indice = 0
            self.funcoes_props = [[self.indice,self.posicao_livre]]

            self.funcoes_nomes = {}
            self.funcoes_nomes[NOME_FUNCAO_RESPOSTA] = self.indice

        with open("nomes_das_funcoes.txt","w") as escritor:
            escritor.write(PROPRIEDADES_FUNCAO_RESPOSTA)

    def resp(self):
        reload(f)
        return f.resp()

calc = Funcoes()

calc.tratamento_para_retorno("x*2 +x**2")