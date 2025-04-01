import flet as ft

import calculadora
from entrada import BotaoDeCalculadora
from entrada import AplicacaoCalculadora
from constantes import TITULO,DIMENSOES,COR_DE_FUNDO

def principal(pagina:  ft.Page):

    app = AplicacaoCalculadora(pagina,TITULO,DIMENSOES,COR_DE_FUNDO)
    app.pagina.on_keyboard_event = app.captura_acao_teclado
    botoes_0 = [
        BotaoDeCalculadora("0",app),
        BotaoDeCalculadora(",",app),
        BotaoDeCalculadora("*10**",app),
        BotaoDeCalculadora("resp",app),
        BotaoDeCalculadora("=",app,"Enter")
    ]

    botoes_1 = [
        BotaoDeCalculadora("1",app),
        BotaoDeCalculadora("2",app),
        BotaoDeCalculadora("3",app),
        BotaoDeCalculadora("+",app),
        BotaoDeCalculadora("-",app)
    ]

    botoes_2 = [
        BotaoDeCalculadora("4",app),
        BotaoDeCalculadora("5",app),
        BotaoDeCalculadora("6",app),
        BotaoDeCalculadora("*",app),
        BotaoDeCalculadora("/",app)
    ]

    botoes_3 = [
        BotaoDeCalculadora("7",app),
        BotaoDeCalculadora("8",app),
        BotaoDeCalculadora("9",app),
        BotaoDeCalculadora("DEL",app),
        BotaoDeCalculadora("AC",app)
    ]

    botoes_4 = [
        BotaoDeCalculadora("ENG",app),
        BotaoDeCalculadora("(",app),
        BotaoDeCalculadora(")",app),
        BotaoDeCalculadora("S<>D",app),
        BotaoDeCalculadora("M+",app)
    ]

    botoes_5 = [
        BotaoDeCalculadora("hyp",app),
        BotaoDeCalculadora("sen",app),
        BotaoDeCalculadora("cos",app),
        BotaoDeCalculadora("tan",app),
        BotaoDeCalculadora("**(1/2)",app)
    ]

    botoes_6 = [
        BotaoDeCalculadora("x**2",app),
        BotaoDeCalculadora("x**",app),
        BotaoDeCalculadora("log",app),
        BotaoDeCalculadora("ln",app),
        BotaoDeCalculadora("**(-1)",app)
    ]

    botoes_7 = [
        BotaoDeCalculadora("pi",app),
        BotaoDeCalculadora("e",app),
        BotaoDeCalculadora("!",app),
        BotaoDeCalculadora("log_x(y)",app),
        BotaoDeCalculadora("**3",app)
    ]

    Linha_0 = ft.Row([
                        app.campo_entrada
                    ])

    Linha_1 = ft.Row([
                      app.texto_entrada
                      ])

    Linha_2 = ft.Row(botoes_7)

    Linha_3 = ft.Row(botoes_6)

    Linha_4 = ft.Row(botoes_5)

    Linha_5 = ft.Row(botoes_4)

    Linha_6 = ft.Row(botoes_3)

    Linha_7 = ft.Row(botoes_2)

    Linha_8 = ft.Row(botoes_1)

    Linha_9 = ft.Row(botoes_0)

    app.pagina.add(ft.Container(width=650,
                                 height=500,
                                 border_radius=ft.border_radius.all(20),
                                 padding=20,
                                 content=ft.Column(
                                     controls=[Linha_0,
                                               Linha_1,
                                               Linha_2,
                                               Linha_3,
                                               Linha_4,
                                               Linha_5,
                                               Linha_6,
                                               Linha_7,
                                               Linha_8,
                                               Linha_9
                                               ]
                                 )
                                 )
                    )

ft.app(principal)
