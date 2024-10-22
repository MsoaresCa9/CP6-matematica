import numpy as np
import matplotlib.pyplot as plt

# Definindo as funções de custo, receita e lucro
def custo(x):
    return 300 + 10 * x**2

def custo_melhorado(x):
    return 100 + 2 * x**2

def receita(x):
    return 90 * x

def lucro(x):
    return receita(x) - custo(x)

def lucro_melhorado(x):
    return receita(x) - custo_melhorado(x)

# Gerando valores para x (quantidade produzida)
x = np.linspace(0, 10, 100)  # Produção de 0 a 10 unidades

# Calculando os valores correspondentes
custo_values = custo(x)
custo_melhorado_values = custo_melhorado(x)
receita_values = receita(x)
lucro_values = lucro(x)
lucro_melhorado_values = lucro_melhorado(x)

# Criando o gráfico
plt.figure(figsize=(12, 8))
plt.plot(x, custo_values, label='Custo Total (C(x))', color='red', linestyle='--')
plt.plot(x, custo_melhorado_values, label='Custo Total Melhorado (C\'(x))', color='orange')
plt.plot(x, receita_values, label='Receita Total (R(x))', color='green')
plt.plot(x, lucro_values, label='Lucro Total (P(x))', color='blue', linestyle='--')
plt.plot(x, lucro_melhorado_values, label='Lucro Total Melhorado (P\'(x))', color='purple')

# Configurando o gráfico
plt.title('Impacto da Redução Significativa de Custos no Lucro Total')
plt.xlabel('Quantidade Produzida (x)')
plt.ylabel('Valor (R$)')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()
plt.grid()
plt.xlim(0, 10)
plt.ylim(-500, 1500)

# Exibindo o gráfico
plt.show()