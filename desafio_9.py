numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

# Calcula o salário
salario = horas_trabalhadas * valor_por_hora

# Imprime o número e o salário formatados
print("NUMBER = ", numero_funcionario)
print("SALARY = U$", f"${salario:.2f}")