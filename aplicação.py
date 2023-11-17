def verifica_multiplos(numero):
    multiplo_de_5 = numero % 5 == 0
    multiplo_de_7 = numero % 7 == 0

    if multiplo_de_5 and multiplo_de_7:
        return "fizzbuzz"
    elif multiplo_de_5:
        return "fizz"
    elif multiplo_de_7:
        return "buzz"
    else:
        return "miss"


def main():
    try:
        numero = int(input("Digite um número natural: "))
        if numero <= 0:
            raise ValueError("Por favor, insira um número natural maior que zero.")

        resultado = verifica_multiplos(numero)
        print(f"Resultado para {numero}: {resultado}")

    except ValueError as e:
        print(f"Erro: {e}")
        print("Certifique-se de inserir um número natural válido.")

if __name__ == "__main__":
    main()

# Testes unitários
assert verifica_multiplos(10) == "fizz"
assert verifica_multiplos(14) == "buzz"
assert verifica_multiplos(35) == "fizzbuzz"
assert verifica_multiplos(8) == "miss"

print("Testes passaram com sucesso!")
