import flet as ft


TITULO = "Solucionador Matemático (by Giovane)"

DIMENSOES = [1216,659]
COR_DE_FUNDO = "#c2c3fc"

BASE_DECIMAL = 10
BASE_BINARIA = 2

NOME_FUNCAO_RESPOSTA = "resp"
RESPOSTA_PADRAO_FUNCAO_RESPOSTA = "0"
FUNCAO_RESPOSTA = (f"def {NOME_FUNCAO_RESPOSTA}():\n"+
                      f"\treturn {RESPOSTA_PADRAO_FUNCAO_RESPOSTA}\n"
                      )

LISTA_FUNCOES_ESPECIAIS = ["factorial","sqrt","comb","exp","log","fsum",
                           "degrees","radians","cos","sin","tan","pi",
                           "e","cbrt"]

IMPORT_ARQUIVO_FUNCOES = ("from math import (factorial, sqrt, comb, exp, log, fsum,\n"
                          "\t\t\t\t  degrees, radians, cos, sin, tan, pi, e,\n"
                          "\t\t\t\t  cbrt)\n\n")


PROPRIEDADES_FUNCAO_RESPOSTA = (f"{NOME_FUNCAO_RESPOSTA},{RESPOSTA_PADRAO_FUNCAO_RESPOSTA},"
                                f"{RESPOSTA_PADRAO_FUNCAO_RESPOSTA},{len(IMPORT_ARQUIVO_FUNCOES)},"
                                f"{len(IMPORT_ARQUIVO_FUNCOES) +
                                   len(FUNCAO_RESPOSTA)},0\n")

ARQUIVO_FUNCOES = "funcoes.py"
ARQUIVO_TXT = "nomes_das_funcoes.txt"

CLASSE_1 = ft.core.control_event.ControlEvent

COMPRIMENTO_DA_MANTISSA = 100
