import pandas as pd
import matplotlib.pyplot as plt

# Caminho para o arquivo CSV
df = pd.read_csv(r'C:\Users\Natan\Desktop\projeto-victor-python\vendas_nike_2008.csv')


#Removendo todas as linhas do DataFrame df que contêm valores nulos (NaN)
df = df.dropna()

#Agrupando os dados do DataFrame df pela coluna 'Mês' e calculando a soma das vendas em milhões de dólares para cada mês
vendas_mes = df.groupby(df['Mês'])['Vendas (em milhões de dólares)'].sum()

# Gráfico em linha
plt.figure(figsize=(10, 6))
plt.plot(vendas_mes.index, vendas_mes.values, marker='o')
plt.xlabel('Mês')
plt.ylabel('Total de vendas (em milhões de dólares)')
plt.title('Vendas Mensais da Nike em 2008')
plt.xticks(range(1, 13), ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'], rotation=45)
plt.grid(True)
plt.show()
