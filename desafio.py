# Solicita ao usuario que digite seu nome
nome_usuario = input("Digite o seu nome: ")

#Solicite ao usuario que digite o valor do seu salário
#Converte a entrada para um número de ponto flutuante

salario_usuario = float(input("Digite o seu salário: "))

# Solicite ao usuario que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o seu bonus: "))

# Calcule o valor do bônus final 
valor_do_bonus = 1000 + salario_usuario * bonus_usuario

# Imprime a mensagem personalizada incluindo o nome do usuario e o valor
print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus}")

# Bônus: Quantos bugs e riscos você consegue indentificar nesse programa?