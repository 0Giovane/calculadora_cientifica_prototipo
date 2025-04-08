from importlib import reload
from typing import Any

import funcoes as f
from constantes import (FUNCAO_RESPOSTA,
                        NOME_FUNCAO_RESPOSTA,
                        PROPRIEDADES_FUNCAO_RESPOSTA,
                        ARQUIVO_FUNCOES,
                        ARQUIVO_TXT,
                        IMPORT_ARQUIVO_FUNCOES,
                        LISTA_FUNCOES_ESPECIAIS,
                        RESPOSTA_PADRAO_FUNCAO_RESPOSTA)


class Funcoes:
    def __init__(self):
        self.__posicao_livre = 0
        self.__funcoes_props = {}
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
    def funcoes_props(self) -> dict[Any, Any]:
        return self.__funcoes_props

    @funcoes_props.setter
    def funcoes_props(self, valor) -> None:
        self.__funcoes_props = valor

    @property
    def indice(self) -> int:
        return self.__indice

    @indice.setter
    def indice(self, valor) -> None:
        self.__indice = valor

    # ================================================================

    def atualiza_nomes(self) -> None:

        with open(ARQUIVO_TXT) as arquivo:
            linhas = arquivo.readlines()
            if len(linhas) != 0:
                for linha in linhas:
                    entrada = linha.strip()
                    valor = entrada.split(",")
                    self.indice += 1
                    self.funcoes_props[valor[0]] = [
                        valor[1],float(valor[2]),
                        int(valor[3]), int(valor[4]),
                        int(valor[5])
                    ]
                    if self.indice + 1 == len(linhas):
                        self.posicao_livre = valor[4]
            else:
                self.reiniciar()

    def reiniciar(self) -> None:

        with (open(ARQUIVO_FUNCOES, "w") as editor):
            editor.write(IMPORT_ARQUIVO_FUNCOES + FUNCAO_RESPOSTA)
            editor.flush()

            self.posicao_livre = (len(IMPORT_ARQUIVO_FUNCOES)
                                  + len(FUNCAO_RESPOSTA))

            self.indice = 0

            # funcoes_props {"resp":[resposta na forma escrita
            # , resposta na forma numérica, posição inicial,
            # posição final,indice]}
            self.funcoes_props = {NOME_FUNCAO_RESPOSTA:[
                 RESPOSTA_PADRAO_FUNCAO_RESPOSTA,
                 RESPOSTA_PADRAO_FUNCAO_RESPOSTA,
                 len(IMPORT_ARQUIVO_FUNCOES),
                 self.posicao_livre,
                 self.indice]}

        with open(ARQUIVO_TXT, "w") as escritor:
            escritor.write(PROPRIEDADES_FUNCAO_RESPOSTA)
            escritor.flush()

    # ================================================================

    def nova_funcao(self, nome_fantasia: str,
                    resultado: str,
                    resultado_entrada: str) -> None:
        nome_da_funcao = self.tratamento_para_nome(nome_fantasia)
        with open(ARQUIVO_FUNCOES, "a") as arquivo:
            self.clean_resp()

            posicao_comeco = self.posicao_livre

            string = (f"def {nome_da_funcao}():\n" +
                      f"\treturn {resultado}\n"
                      )

            posicao_final = posicao_comeco + len(string)

            arquivo.write(string)
            arquivo.flush()

            self.indice += 1
            indice_funcao = self.indice

            self.anexar_resp(nome_da_funcao,
                             posicao_final, nome_fantasia)
            self.corrige_props_resposta(nome_fantasia,
                                        resultado_entrada,
                                        posicao_comeco,
                                        posicao_final,
                                        indice_funcao)

    def editar_funcao(self, nome_fantasia: str,
                      resultado: str,
                      resultado_entrada: str) -> None:
        nome_da_funcao = self.tratamento_para_nome(nome_fantasia)
        self.clean_resp()
        with open(ARQUIVO_FUNCOES) as leitor:
            original = leitor.read()

        with open(ARQUIVO_FUNCOES, "w") as editor:
            indice = self.funcoes_props[nome_fantasia][-1]

            posicao_comeco = self.funcoes_props[nome_fantasia][2]
            posicao_final = self.funcoes_props[nome_fantasia][3]

            string = (f"def {nome_da_funcao}():\n" +
                      f"\treturn {resultado}\n"
                      )

            original = (original[:posicao_comeco] +
                        string +
                        original[posicao_final:]
                        )

            editor.write(original)
            editor.flush()

            posicao_final = posicao_comeco + len(string)

            self.corrige_posicoes(indice, posicao_final)
            self.anexar_resp(nome_da_funcao,
                             self.posicao_livre, nome_fantasia)
            self.corrige_props_resposta(nome_fantasia,
                                        resultado_entrada,
                                        posicao_comeco,
                                        posicao_final,
                                        indice,
                                        True)

    def corrige_posicoes(self, indice, posicao_referencia) -> None:

        with (open(ARQUIVO_TXT) as leitura):
            linhas = leitura.readlines()

        propriedades = [linha.strip().split(",") for linha in linhas]

        for posicao in range(indice + 1, len(self.funcoes_props)):

            nome_atual = propriedades[posicao][0]
            comprimento = (self.funcoes_props[nome_atual][3] -
                           self.funcoes_props[nome_atual][2])

            self.funcoes_props[nome_atual][2] = posicao_referencia
            propriedades[posicao][3] = str(posicao_referencia)

            posicao_referencia = posicao_referencia + comprimento

            self.funcoes_props[nome_atual][3] = posicao_referencia
            propriedades[posicao][4] = str(posicao_referencia)

        self.posicao_livre = posicao_referencia
        string_saida = ""
        for linha in propriedades:
            for elemento in linha:
                string_saida += elemento + ","
            string_saida = string_saida[:len(string_saida) - 1]
            string_saida += "\n"

        with open(ARQUIVO_TXT, "w") as escritor:
            escritor.write(string_saida)
            escritor.flush()

    def corrige_props_resposta(self, nome_fantasia: str,
                               resultado: str,
                               posicao_comeco: int,
                               posicao_final: int,
                               indice_funcao: int,
                               edicao=False) -> None:

        with open(ARQUIVO_TXT) as props:
            propriedades = props.readlines()

        resposta = self.resp()

        self.funcoes_props[nome_fantasia] = [
            resultado, resposta,
            posicao_comeco, posicao_final,
            indice_funcao
        ]
        string_props = (f"{nome_fantasia},{resultado},{resposta},"
                        f"{posicao_comeco},{posicao_final},"
                        f"{indice_funcao}\n")
        if not edicao:
            propriedades.insert(-1, string_props)
        else:
            propriedades[indice_funcao] = string_props

        with open(ARQUIVO_TXT, "w") as escritor:
            string = ""
            for linha in propriedades:
                string += linha
            escritor.write(string)
            escritor.flush()

    # ================================================================

    @staticmethod
    def tratamento_para_nome(nome) -> str:
        return nome if (nome == NOME_FUNCAO_RESPOSTA) else f"_{nome}"

    @staticmethod
    def tratamento_nomes_fantasia(nome_fantasia):
        if (nome_fantasia != NOME_FUNCAO_RESPOSTA and
                ((nome_fantasia.isdigit()) or (
                nome_fantasia in LISTA_FUNCOES_ESPECIAIS))):
            nome_fantasia = f"_{nome_fantasia}"
        return nome_fantasia

    def tratamento_para_retorno(self, retorno) -> str:
        string = retorno
        for nome in self.funcoes_props:

            fragmento_do_retorno = string
            acrescimo = 0

            while nome in fragmento_do_retorno:
                posicao_inicial_fragmento_de_retorno = (
                    fragmento_do_retorno.find(nome))
                posicao_final_fragmento_de_retorno = (
                    posicao_inicial_fragmento_de_retorno + len(nome))

                fragmento_do_retorno = (
                  fragmento_do_retorno[
                    :posicao_inicial_fragmento_de_retorno] +
                  fragmento_do_retorno[
                    posicao_final_fragmento_de_retorno:])

                posicao_inicial = (acrescimo +
                                   posicao_inicial_fragmento_de_retorno)
                posicao_final = (acrescimo +
                                 posicao_final_fragmento_de_retorno)

                if nome != NOME_FUNCAO_RESPOSTA:
                    acrescimo += 3 + len(nome)
                    string = (string[:posicao_inicial] + "_" +
                              f"{nome}" + "()" +
                              string[posicao_final:])
                else:
                    resposta = str(self.resp())
                    acrescimo += len(resposta)
                    string = (string[:posicao_inicial] +
                              f"{resposta}" + string[posicao_final:])

        return string

    # ================================================================

    def fabrica_funcoes(self, nome_fantasia, resultado) -> None:

        nome_fantasia = self.tratamento_nomes_fantasia(nome_fantasia)
        resp = self.tratamento_para_retorno(resultado)

        if nome_fantasia == NOME_FUNCAO_RESPOSTA:
            self.modifica_resp(resp,resultado)
        elif nome_fantasia in self.funcoes_props:
            self.editar_funcao(nome_fantasia, resp, resultado)
        else:
            self.nova_funcao(nome_fantasia, resp, resultado)

    # ================================================================

    def clean_resp(self):
        with open(ARQUIVO_TXT) as leitura:
            posicao = self.funcoes_props[NOME_FUNCAO_RESPOSTA][-1]
            linhas = leitura.readlines()
            linha = linhas[posicao].strip().split(",")
            vetor_resp = [int(linha[3]), int(linha[4])]

        with open(ARQUIVO_TXT, "w") as escritor:
            string_txt = ""
            pos = 0
            while pos < len(linhas):
                if pos != posicao:
                    string_txt += linhas[pos]
                pos += 1
            escritor.write(string_txt)
            escritor.flush()

        with open(ARQUIVO_FUNCOES) as leitor:
            original = leitor.read()

        with (open(ARQUIVO_FUNCOES, "w") as editor):

            string = (original[:vetor_resp[0]] +
                      original[vetor_resp[1]:])
            editor.write(string)
            editor.flush()

        self.funcoes_props.pop(NOME_FUNCAO_RESPOSTA)
        self.indice -= 1
        self.posicao_livre = vetor_resp[0]

    def anexar_resp(self,nome_da_funcao,
                    posicao_inicial,nome_fantasia):
        with (open(ARQUIVO_FUNCOES,"a") as arquivo):
            resp = (f"def {NOME_FUNCAO_RESPOSTA}():\n" +
                    f"\treturn {nome_da_funcao}()\n"
                    )
            arquivo.write(resp)
            arquivo.flush()
            self.posicao_livre = posicao_inicial + len(resp)
            self.indice += 1
            resposta = self.resp()
            self.funcoes_props[NOME_FUNCAO_RESPOSTA] = (
                [nome_fantasia,
                    resposta,
                    posicao_inicial,
                    self.posicao_livre,
                    self.indice]
            )

        with open(ARQUIVO_TXT,"a") as props:
            props.write(f"{NOME_FUNCAO_RESPOSTA},"
                        f"{nome_fantasia},"
                        f"{resposta},"
                        f"{posicao_inicial},{self.posicao_livre},"
                        f"{self.indice}\n")
            props.flush()

    def modifica_resp(self, retorno: str,
                      retorno_entrada: str) -> None:
        indice = self.funcoes_props[NOME_FUNCAO_RESPOSTA][-1]
        posicao_inicial = self.funcoes_props[NOME_FUNCAO_RESPOSTA][2]

        with open(ARQUIVO_FUNCOES) as leitura:
            original = leitura.read()
        with open(ARQUIVO_TXT) as leitor:
            original_txt = leitor.readlines()

        with open(ARQUIVO_FUNCOES,"w") as editor:
            resp = (f"def {NOME_FUNCAO_RESPOSTA}():\n" +
                    f"\treturn {retorno}\n"
                    )

            string = (original[:posicao_inicial] +
                      resp)

            self.posicao_livre = posicao_inicial + len(resp)
            self.funcoes_props[NOME_FUNCAO_RESPOSTA][3] = (
                self.posicao_livre)
            editor.write(string)
            editor.flush()

        resposta = self.resp()

        self.funcoes_props[NOME_FUNCAO_RESPOSTA][0] = retorno_entrada
        self.funcoes_props[NOME_FUNCAO_RESPOSTA][1] = resposta

        with open(ARQUIVO_TXT,"w") as escritor:
            original_txt[indice] = (f"{NOME_FUNCAO_RESPOSTA},"
                                    f"{retorno_entrada},{resposta},"
                                    f"{posicao_inicial},"
                                    f"{self.posicao_livre},"
                                    f"{indice}\n")
            string = ""
            for linha in original_txt:
                string += linha
            escritor.write(string)
            escritor.flush()

    def resp(self, funcao: str = "") -> Any:
        if funcao != "" and funcao != NOME_FUNCAO_RESPOSTA:
            if funcao in self.funcoes_props:
                nome = self.tratamento_para_nome(funcao)
                self.modifica_resp(nome + "()",nome)
            else:
                self.nova_funcao(funcao,"0", "0")
        reload(f)
        return f.resp()
