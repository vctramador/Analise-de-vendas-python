import pandas as pd

# Dados fictícios de vendas da Nike em produtos esportivos de futebol em 2008
data = {
    'Mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    'Vendas (em milhões de dólares)': [10, 12, 15, 18, 20, 22, 25, 28, 30, 28, 25, 20]
}

df = pd.DataFrame(data)

# Salvando os dados em um arquivo CSV
df.to_csv('vendas_nike_2008.csv', index=False)
