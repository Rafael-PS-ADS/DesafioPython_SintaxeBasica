def calcular_salario_liquido():
    try:
        valorSalario = float(input("Digite o valor bruto do salário: "))
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")
        return

    try:
        valorBeneficios = float(input("Digite o valor adicional dos benefícios: "))
    except ValueError:
        print("Entrada inválida para os benefícios. Por favor, digite um número.")
        return

    valorImposto = 0.0

    if 0 <= valorSalario <= 1100:
        valorImposto = 0.05 * valorSalario
    elif 1100 < valorSalario <= 2500:
        valorImposto = 0.10 * valorSalario
    else:
        valorImposto = 0.15 * valorSalario
    
    saida = valorSalario - valorImposto + valorBeneficios

    print(f"O valor a ser transferido é: {saida:.2f}")

if __name__ == "__main__":
    calcular_salario_liquido()