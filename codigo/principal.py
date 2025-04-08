import flet as ft

from entrada import (BotaoDeCalculadora,
                     AplicacaoCalculadora)
from constantes import (TITULO,
                        DIMENSOES,
                        COR_DE_FUNDO)


def principal(pagina: ft.Page):
    app = AplicacaoCalculadora(pagina,
                               TITULO,
                               DIMENSOES,
                               COR_DE_FUNDO)
    app.pagina.on_keyboard_event = app.captura_acao_teclado

    botoes_0 = [
        BotaoDeCalculadora("0", app),
        BotaoDeCalculadora(".", app),
        BotaoDeCalculadora("*10**", app),
        BotaoDeCalculadora("=", app),
        BotaoDeCalculadora("resp", app, "Enter")
    ]

    botoes_1 = [
        BotaoDeCalculadora("1", app),
        BotaoDeCalculadora("2", app),
        BotaoDeCalculadora("3", app),
        BotaoDeCalculadora("+", app),
        BotaoDeCalculadora("-", app)
    ]

    botoes_2 = [
        BotaoDeCalculadora("4", app),
        BotaoDeCalculadora("5", app),
        BotaoDeCalculadora("6", app),
        BotaoDeCalculadora("*", app),
        BotaoDeCalculadora("/", app)
    ]

    botoes_3 = [
        BotaoDeCalculadora("7", app),
        BotaoDeCalculadora("8", app),
        BotaoDeCalculadora("9", app),
        BotaoDeCalculadora("DEL", app),
        BotaoDeCalculadora("AC", app, "Reset: Shift + Del")
    ]

    botoes_4 = [
        BotaoDeCalculadora("ENG", app),
        BotaoDeCalculadora("(", app),
        BotaoDeCalculadora(")", app),
        BotaoDeCalculadora("S<>D", app),
        BotaoDeCalculadora("M+", app)
    ]

    botoes_5 = [
        BotaoDeCalculadora("cbrt()", app,"raiz cúbica"),
        BotaoDeCalculadora("sin()", app),
        BotaoDeCalculadora("cos()", app),
        BotaoDeCalculadora("tan()", app),
        BotaoDeCalculadora("sqrt()", app,"raiz quadrada")
    ]

    botoes_6 = [
        BotaoDeCalculadora("**2", app),
        BotaoDeCalculadora("**", app),
        BotaoDeCalculadora("log(, 10)", app),
        BotaoDeCalculadora("log(, e)", app),
        BotaoDeCalculadora("**(-1)", app)
    ]

    botoes_7 = [
        BotaoDeCalculadora("pi", app),
        BotaoDeCalculadora("e", app),
        BotaoDeCalculadora("factorial()", app),
        BotaoDeCalculadora("log(, )", app,"log(variável, base)"),
        BotaoDeCalculadora("**3", app)
    ]

    linha_0 = ft.Row([
        app.campo_entrada
    ])

    linha_1 = ft.Row([
        app.texto_entrada
    ])

    linha_2 = ft.Row(botoes_7)

    linha_3 = ft.Row(botoes_6)

    linha_4 = ft.Row(botoes_5)

    linha_5 = ft.Row(botoes_4)

    linha_6 = ft.Row(botoes_3)

    linha_7 = ft.Row(botoes_2)

    linha_8 = ft.Row(botoes_1)

    linha_9 = ft.Row(botoes_0)

    coluna_1 = ft.Column(
                        controls=[linha_0,
                                  linha_1,
                                  linha_2,
                                  linha_3,
                                  linha_4,
                                  linha_5,
                                  linha_6,
                                  linha_7,
                                  linha_8,
                                  linha_9
                                  ]
                        )

    funcoes = ft.Container(width=200,
                             height=500,
                             border_radius=ft.border_radius.all(20),
                             bgcolor=ft.Colors.BLUE_50,
                             padding=20,
                             content=app.historico_funcoes
                             )

    historico = ft.Container(width=200,
                             height=500,
                             border_radius=ft.border_radius.all(20),
                             bgcolor=ft.Colors.AMBER,
                             padding=20,
                             content=app.historico
                             )

    exibicao_calculadora = ft.Container(width=650,
                                        height=500,
                                        border_radius=ft.border_radius.all(20),
                                        padding=20,
                                        content= coluna_1
                                        )


    linha = ft.Row([funcoes,
                    ft.VerticalDivider(),
                    historico,
                    ft.VerticalDivider(),
                    exibicao_calculadora])

    app.pagina.add(linha)


ft.app(principal)
