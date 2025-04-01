import calculadora

calc = calculadora.Funcoes()
calc.reiniciar()

def seletor(a):
    entrada = list(a)
    if len(entrada) == 2:
        calc.fabrica_funcoes(entrada[0],entrada[1])
    if a[0] == " ":
        print(calc.resp())

a = input().split("=")

while a != [""]:
    seletor(a)
    a = input().split("=")

