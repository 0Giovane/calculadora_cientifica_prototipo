import flet as ft


import calculadora
from codigo.constantes import NOME_FUNCAO_RESPOSTA
from constantes import CLASSE_1

class AplicacaoCalculadora:

    def __init__(self, pagina, titulo, coords, cor_de_fundo) -> None:
        self.__pagina = pagina

        self.__campo_entrada = (
            ft.TextField("",
                         hint_text="x = 0",
                         autofocus=True,
                         multiline=True,
                         shift_enter=True,
                         smart_quotes_type=True,
                         on_submit=self.enviar_entrada,
                         )
        )

        self.__texto_entrada = ft.Text("")

        self.define_layout(titulo,
                           coords,
                           cor_de_fundo)

        self.__calculadora = calculadora.Funcoes()

    # ================================================================

    @property
    def pagina(self) -> ft.Page:
        return self.__pagina

    @pagina.setter
    def pagina(self, valor) -> None:
        self.__pagina = valor

    @property
    def campo_entrada(self) -> ft.TextField:
        return self.__campo_entrada

    @campo_entrada.setter
    def campo_entrada(self, valor) -> None:
        self.__campo_entrada = valor

    @property
    def texto_entrada(self) -> ft.Text:
        return self.__texto_entrada

    @texto_entrada.setter
    def texto_entrada(self, valor) -> None:
        self.__texto_entrada = valor

    @property
    def calculadora(self):
        return self.__calculadora

    @calculadora.setter
    def calculadora(self, valor):
        self.__calculadora = valor

    # ================================================================

    def define_layout(self, titulo: str,
                      coords: list[int, int],
                      cor_de_fundo: str) -> None:

        self.pagina.title = titulo
        self.pagina.window.width = coords[0]
        self.pagina.window.height = coords[1]
        self.pagina.bgcolor = cor_de_fundo

    def captura_acao_teclado(self,
                             tecla: ft.KeyboardEvent) -> None:
        if tecla.key == "Delete" and tecla.shift:
            self.reiniciar_calculadora()

    def enviar_entrada(self,elemento):
        self.texto_entrada.value = self.calcular()
        elemento.control.value = ""
        self.pagina.update()
    def enviar_entrada_botao(self):
        self.texto_entrada.value = self.calcular()
        self.campo_entrada.value = ""
        self.pagina.update()
    def reiniciar_calculadora(self) -> None:
        self.calculadora.reiniciar()
        self.texto_entrada.value = ""
        self.campo_entrada.value = ""

    def possui_igual(self, string: str) -> str:
        if "=" in string:
            return string
        else:
            if NOME_FUNCAO_RESPOSTA in string:
                while NOME_FUNCAO_RESPOSTA in string:
                    posicao = string.find(NOME_FUNCAO_RESPOSTA)
                    string = (
                            string[:posicao] +
                            f"{self.calculadora.resp()}" +
                            string[posicao + len(NOME_FUNCAO_RESPOSTA):])
            return f"{NOME_FUNCAO_RESPOSTA}=" + string

    def retorna_nome_e_resultado(self,string):
        posicao = string.find("=")
        nome = string[:posicao]
        resultado = string[posicao + 1:]
        return nome, resultado

    def sanitiza_entrada(self) -> tuple[str, str]:
        pre_tratamento = self.campo_entrada.value.replace(" ", "")
        pre_tratamento = self.campo_entrada.value.replace("\n", "")
        string = self.possui_igual(pre_tratamento)
        return self.retorna_nome_e_resultado(string)

    def calcular(self) -> str:
        nome, resultado = self.sanitiza_entrada()
        self.calculadora.fabrica_funcoes(nome, resultado)
        return f"{nome} = {self.calculadora.resp()}"


class BotaoDeCalculadora(ft.ElevatedButton):
    def __init__(self, texto: str,
                 app: AplicacaoCalculadora,
                 dica: str = "",
                 expancao: int = 1) -> None:
        super().__init__()
        self.text = texto
        self.expand = expancao
        self.on_click = self.botao_clicado
        self.data = texto
        self.app = app
        self.tooltip = dica

    def botao_clicado(self, elemento: CLASSE_1) -> None:
        s = elemento.control.data
        match s:
            case "AC":
                self.app.reiniciar_calculadora()
            case "=":
                self.app.enviar_entrada_botao()
            case _:
                self.app.campo_entrada.value += s
        self.app.pagina.update()

