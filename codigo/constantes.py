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
PROPRIEDADES_FUNCAO_RESPOSTA = (f"resp,0,{len(FUNCAO_RESPOSTA)}\n")

ARQUIVO_FUNCOES = "funcoes.py"
ARQUIVO_TXT = "nomes_das_funcoes.txt"

CLASSE_1 = ft.core.control_event.ControlEvent

COMPRIMENTO_DA_MANTISSA = 100
