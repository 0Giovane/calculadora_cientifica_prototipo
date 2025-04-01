import flet as ft

import calculadora
from constantes import NOME_FUNCAO_RESPOSTA


class BotaoDeCalculadora(ft.ElevatedButton):
    def __init__(self,texto,app,dica="",expancao=1):
        super().__init__()
        self.text = texto
        self.expand = expancao
        self.on_click = self.botao_clicado
        self.data = texto
        self.app = app
        self.tooltip = dica

    def botao_clicado(self,elemento):
        s = elemento.control.data
        if s == "AC":
            self.app.reiniciar_calculadora()
        else:
            self.app.campo_entrada.value += s
        self.app.pagina.update()

class AplicacaoCalculadora:

    def __init__(self,pagina,titulo,coords,cor_de_fundo):
        self.__pagina = pagina

        self.__campo_entrada = (
        ft.TextField("",hint_text="x = 0",multiline=True)
        )

        self.__texto_entrada = ft.Text("")

        self.define_layout(titulo,coords,cor_de_fundo)

    # ================================================================

    @property
    def pagina(self):
        return self.__pagina

    @pagina.setter
    def pagina(self, valor):
        self.__pagina = valor

    @property
    def campo_entrada(self):
        return self.__campo_entrada

    @campo_entrada.setter
    def campo_entrada(self, valor):
        self.__campo_entrada = valor

    @property
    def texto_entrada(self):
        return self.__texto_entrada

    @texto_entrada.setter
    def texto_entrada(self, valor):
        self.__texto_entrada = valor

    # ================================================================

    def define_layout(self,titulo,coords,cor_de_fundo):

        self.pagina.title = titulo
        self.pagina.window.width = coords[0]
        self.pagina.window.height = coords[1]
        self.pagina.bgcolor = cor_de_fundo

    def captura_acao_teclado(self,tecla: ft.KeyboardEvent):
        if tecla.key == "Enter":
            valor = self.calcular()
            self.campo_entrada.value = ""
            self.texto_entrada.value = valor
            self.pagina.update()
        elif tecla.key == "Delete" and tecla.shift:
            self.reiniciar_calculadora()

    def reiniciar_calculadora(self):
        calc = calculadora.Funcoes()
        calc.reiniciar()
        self.texto_entrada.value = ""

    def possui_igual(self,string):
        if "=" in string:
            return string
        else:
            if "x" in string:
                while "x" in string:
                    posicao = string.find("x")
                    calc = calculadora.Funcoes()
                    string = string[:posicao] + f"{calc.resp()}" + string[posicao + 3:]
            return "x=" + string


    def sanitiza_entrada(self):
        string = self.possui_igual(self.campo_entrada.value.replace(" ",""))
        vetor = string.split("=")
        nome,resultado = vetor[0],vetor[1]
        return nome,resultado

    def calcular(self):
        calc = calculadora.Funcoes()
        nome,resultado = self.sanitiza_entrada()
        calc.fabrica_funcoes(nome,resultado)
        return f"{nome} = {calc.resp()}"
