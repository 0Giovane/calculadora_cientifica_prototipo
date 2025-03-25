a = input()
b = input()
base =10
tamanho_mantissa = 100



def tratamento(num,exp,entrada) -> tuple:
    if "." in entrada:
        vetores = entrada.split(".")
        if vetores[0]:
            inteiros = int(vetores[0])
        else:
            inteiros = 0

        decimais = [int(char) for char in vetores[1]]

        if inteiros:
            inteiros = str(inteiros)
            inteiros = [int(char) for char in inteiros]
            exp = len(inteiros)
            num = inteiros + decimais
        else:
            i = 0
            for num in decimais:
                if num:
                    exp = i
                    break

                i -= 1

            if vetores[1]:
                decimais = int(vetores[1])
            else:
                decimais = 0

            decimais = str(decimais)

            decimais = [int(char) for char in decimais]
            num = decimais

    else:
        num = [int(char) for char in entrada]
        exp = len(num)
    return num,exp



#inserir numeros na mantissa
def corrige_mantissa(mantissa,num) -> None:
    k = 0
    while len(num) > k < len(mantissa):
        mantissa[k] = num[k]
        k += 1
    return mantissa


def retorna_mantissa_texto(mantissa) -> str:
    numero_impresso = ""
    p = 0
    while p < len(mantissa):
        numero = mantissa[p]
        contador_de_zero = 0
        if numero:
            numero_impresso += str(numero)
        else:
            contador_de_zero += 1
            while p < len(mantissa) - 1 and (not numero):
                p += 1
                numero = mantissa[p]
                if numero:
                    numero_impresso += ("0"*contador_de_zero) + str(numero)
                else:
                    contador_de_zero += 1
        p += 1
    return numero_impresso

def somar(a,exp_a,b,exp_b):

    maior = menor = 0
    mantissa = [0]*tamanho_mantissa
    exp = 0

    if exp_a > exp_b:
        maior = exp_a
        menor = exp_b
    else:
        maior = exp_b
        menor = exp_a

    exp = maior

    for var in range(maior - menor):
        if menor == exp_a:
            a.insert(0,0)
            a.pop()
        else:
            b.insert(0, 0)
            b.pop()

    for var in range(tamanho_mantissa-1,-1,-1):

        valor = a[var] + b[var]

        if valor >= base:
            valor = valor - base
            pos = var - 1
            if pos > -1:
                a[pos] += 1
            else:
                mantissa.insert(0,1)
                mantissa.pop()

        mantissa[var] = valor

    return mantissa,exp



if __name__ == "__main__":

    mantissa_a = [0]*tamanho_mantissa
    mantissa_b = [0]*tamanho_mantissa

    num_a,exp_a = tratamento([],0,a)
    num_b,exp_b = tratamento([],0,b)

    mantissa_a = corrige_mantissa(mantissa_a,num_a)
    mantissa_b = corrige_mantissa(mantissa_b, num_b)

    numero_impresso_a = retorna_mantissa_texto(mantissa_a)
    numero_impresso_b = retorna_mantissa_texto(mantissa_b)

    print(f"a = 0.{numero_impresso_a} x {base} ^ ( {exp_a} )")
    print(f"b = 0.{numero_impresso_b} x {base} ^ ( {exp_b} )")

    mantissa_soma,exp_soma = somar(mantissa_a, exp_a, mantissa_b, exp_b)
    numero_impresso_soma = retorna_mantissa_texto(mantissa_soma)

    print(f"soma = 0.{numero_impresso_soma} x {base} ^ ( {exp_soma} )")
