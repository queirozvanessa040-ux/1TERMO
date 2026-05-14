# Exercício 7

 # Pedindo as informações para o usuário 
Total_produzido = float(input("Digite a quantidade total de peças produzidas: ")) 
pecas_defeituosas = float(input("Digite a quantidade de peças defeituosas: ")) 

# Calculando a quantidade de peças boas 
Peças_boas = Total_produzido - pecas_defeituosas

# Calculando a taxa de aproveitamento (em porcentagem) 
Taxa_aproveitamento = (Peças_boas / Total_produzido) * 100 

# Exibindo os resultados 
print("-" * 30) 
print(f"Total de peças boas: {Peças_boas}") 
print(f"Taxa de aproveitamento: {Taxa_aproveitamento:.2f}%")