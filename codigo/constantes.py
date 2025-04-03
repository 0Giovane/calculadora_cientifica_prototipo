import flet as ft


TITULO = "Solucionador Matemático (by Giovane)"

DIMENSOES = [516,659]
COR_DE_FUNDO = "#c2c3fc"

BASE_DECIMAL = 10
BASE_BINARIA = 2

NOME_FUNCAO_RESPOSTA = "resp"
FUNCAO_RESPOSTA = ("def resp():\n"+
                      f"\treturn 0\n"
                      )

IMPORT_ARQUIVO_FUNCOES = ("from math import factorial, "
                          "sqrt, comb, exp, log, fsum, degrees, "
                          "radians, cos, sin, tan, pi, e, cbrt\n\n")

PROPRIEDADES_FUNCAO_RESPOSTA = (f"resp,{len(IMPORT_ARQUIVO_FUNCOES)},"
                                f"{len(IMPORT_ARQUIVO_FUNCOES) +
                                   len(FUNCAO_RESPOSTA)}\n")

ARQUIVO_FUNCOES = "funcoes.py"
ARQUIVO_TXT = "nomes_das_funcoes.txt"

CLASSE_1 = ft.core.control_event.ControlEvent

COMPRIMENTO_DA_MANTISSA = 100
