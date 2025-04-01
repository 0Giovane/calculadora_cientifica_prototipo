from importlib import reload
from typing import Any

import funcoes as f
from constantes import (FUNCAO_RESPOSTA,
                        NOME_FUNCAO_RESPOSTA,
                        PROPRIEDADES_FUNCAO_RESPOSTA,
                        ARQUIVO_FUNCOES,
                        ARQUIVO_TXT)


class Funcoes:
    def __init__(self):
        self.__posicao_livre = 0
        self.__funcoes_props = []
        self.__funcoes_nomes = {}
        self.__indice = -1
        self.atualiza_nomes()

    # ================================================================
    @property
    def posicao_livre(self) -> int:
        return self.__posicao_livre

    @posicao_livre.setter
    def posicao_livre(self, valor) -> None:
        self.__posicao_livre = valor

    @property
    def funcoes_props(self) -> list[Any]:
        return self.__funcoes_props

    @funcoes_props.setter
    def funcoes_props(self, valor) -> None:
        self.__funcoes_props = valor

    @property
    def funcoes_nomes(self) -> dict[Any, Any]:
        return self.__funcoes_nomes

    @funcoes_nomes.setter
    def funcoes_nomes(self, valor) -> None:
        self.__funcoes_nomes = valor

    @property
    def indice(self) -> int:
        return self.__indice

    @indice.setter
    def indice(self, valor) -> None:
        self.__indice = valor

    # ================================================================

    def atualiza_nomes(self) -> None:

        with open(ARQUIVO_TXT) as arquivo:
            for linha in arquivo.readlines():
                entrada = linha.strip()
                valor = entrada.split(",")
                self.indice += 1
                self.funcoes_props.append(list(map(int, [valor[1], valor[2]])))
                self.funcoes_nomes[valor[0]] = self.indice
            if len(self.funcoes_props) > 0:
                self.posicao_livre = self.funcoes_props[-1][1]

    def nova_funcao(self, nome_da_funcao: str,
                    resultado: str,
                    nome_fantasia: str) -> None:

        with open(ARQUIVO_FUNCOES, "a") as arquivo:
            self.clean_resp()
            posicao_comeco = self.posicao_livre

            string = (f"def {nome_da_funcao}():\n" +
                      f"\treturn {resultado}\n"
                      )

            arquivo.write(string)

            posicao_final = posicao_comeco + len(string)
            self.indice += 1

            self.funcoes_props.append([posicao_comeco, posicao_final])
            self.funcoes_nomes[nome_fantasia] = self.indice

            resp = ("def resp():\n"+
                    f"\treturn {nome_da_funcao}()\n"
                   )
            arquivo.write(resp)

            self.posicao_livre = posicao_final + len(resp)
            self.indice += 1
            self.funcoes_props.append([posicao_final, self.posicao_livre])
            self.funcoes_nomes[NOME_FUNCAO_RESPOSTA] = self.indice

            with open(ARQUIVO_TXT, "a") as nomes:
                nomes.write(nome_fantasia + f",{posicao_comeco},{posicao_final}\n")
                nomes.write("resp" + f",{posicao_final},{self.posicao_livre}\n")

    def editar_funcao(self, nome_da_funcao: str,
                      resultado: str = "0") -> None:
        original = ""
        with open(ARQUIVO_FUNCOES) as leitor:
            original = leitor.read()

        with open(ARQUIVO_FUNCOES, "w") as editor:
            indice = self.funcoes_nomes[nome_da_funcao]

            posicao_comeco = self.funcoes_props[indice][0]
            posicao_final = self.funcoes_props[indice][1]

            string = (f"def {nome_da_funcao}():\n" +
                      f"\treturn {resultado}\n"
                      )

            original = (original[:posicao_comeco] +
                        string +
                        original[posicao_final:]
                        )

            editor.write(original)

            posicao_final = posicao_comeco + len(string)

            self.corrige_posicoes(indice, posicao_final)

    def corrige_posicoes(self, indice, posicao_referencia) -> None:

        self.funcoes_props[indice][1] = posicao_referencia

        with open(ARQUIVO_TXT) as leitura:
            propriedades = [linha.strip().split(",") for linha in leitura.readlines()]
            with open(ARQUIVO_TXT, "w") as escritor:
                propriedades[indice][2] = str(posicao_referencia)

                for posicao in range(indice + 1, len(self.funcoes_props)):

                    comprimento = self.funcoes_props[posicao][1] - self.funcoes_props[posicao][0]

                    self.funcoes_props[posicao][0] = posicao_referencia
                    propriedades[posicao][1] = str(posicao_referencia)

                    posicao_referencia = posicao_referencia + comprimento

                    self.funcoes_props[posicao][1] = posicao_referencia
                    propriedades[posicao][2] = str(posicao_referencia)

                string_saida = ""
                for linha in propriedades:
                    for elemento in linha:
                        string_saida += elemento + ","
                    string_saida = string_saida[:len(string_saida) - 1]
                    string_saida += "\n"
                escritor.write(string_saida)

    @staticmethod
    def tratamento_para_nome(nome) -> str:
        return f"_{nome}"

    def tratamento_para_retorno(self, retorno) -> str:
        string = retorno
        for nome in self.funcoes_nomes:

            fragmento_do_retorno = string
            acrescimo = 0

            while nome in fragmento_do_retorno:
                posicao_inicial_fragmento_de_retorno = fragmento_do_retorno.find(nome)
                posicao_final_fragmento_de_retorno = posicao_inicial_fragmento_de_retorno + len(nome)

                fragmento_do_retorno = (
                        fragmento_do_retorno[:posicao_inicial_fragmento_de_retorno] +
                        fragmento_do_retorno[posicao_final_fragmento_de_retorno:])

                posicao_inicial = acrescimo + posicao_inicial_fragmento_de_retorno
                posicao_final = acrescimo + posicao_final_fragmento_de_retorno

                acrescimo = 3 + len(nome)

                string = string[:posicao_inicial] + "_" + f"{nome}" + "()" + string[posicao_final:]

        return string

    def fabrica_funcoes(self, nome_fantasia, resultado) -> None:

        nome_funcao = Funcoes.tratamento_para_nome(nome_fantasia)
        resp = self.tratamento_para_retorno(resultado)

        if nome_fantasia in self.funcoes_nomes:
            self.editar_funcao(nome_funcao, resp)
        else:
            self.nova_funcao(nome_funcao, resp, nome_fantasia)

        self.editar_funcao("resp", f"{nome_funcao}()")

    def reiniciar(self) -> None:

        with open(ARQUIVO_FUNCOES, "w") as editor:
            editor.write(FUNCAO_RESPOSTA)

            self.posicao_livre = len(FUNCAO_RESPOSTA)

            self.indice = 0
            self.funcoes_props = [[self.indice, self.posicao_livre]]

            self.funcoes_nomes = {NOME_FUNCAO_RESPOSTA: self.indice}

        with open(ARQUIVO_TXT, "w") as escritor:
            escritor.write(PROPRIEDADES_FUNCAO_RESPOSTA)

    def clean_resp(self):

        with open(ARQUIVO_TXT) as leitura:
            original_txt = leitura.read()
            posicao = self.funcoes_nomes[NOME_FUNCAO_RESPOSTA]
            linha = leitura.readline(posicao).strip()
            vetor_resp = linha.split(",")
            vetor_resp = [int(vetor_resp[1]), int(vetor_resp[2])]

        with open(ARQUIVO_TXT, "w") as escritor:
            string_txt = original_txt[len(linha):]
            escritor.write(string_txt)

        with open(ARQUIVO_FUNCOES) as leitor:
            original = leitor.read()

        with open(ARQUIVO_FUNCOES, "w") as editor:
            string = original[:vetor_resp[0]] + original[vetor_resp[1]:]
            editor.write(string)

        self.funcoes_props.pop(posicao)
        self.funcoes_nomes.pop(NOME_FUNCAO_RESPOSTA)
        self.indice -= 1
        self.posicao_livre = vetor_resp[0]



    @staticmethod
    def resp(self) -> Any:
        reload(f)
        return f.resp()

calc = Funcoes()
