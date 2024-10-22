import numpy as np
import matplotlib.pyplot as plt

# Definindo as funções de custo, receita e lucro
def custo(x):
    return 300 + 10 * x**2

def receita(x):
    return 90 * x

def lucro(x):
    return receita(x) - custo(x)

# Gerando valores para x (quantidade produzida)
x = np.linspace(0, 10, 100)  # Produção de 0 a 10 unidades

# Calculando os valores correspondentes
custo_values = custo(x)
receita_values = receita(x)
lucro_values = lucro(x)

# Encontrando o ponto ótimo de produção
ponto_otimo = 4.5  # Aproximadamente 5 unidades
lucro_otimo = lucro(ponto_otimo)

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, custo_values, label='Custo Total (C(x))', color='red')
plt.plot(x, receita_values, label='Receita Total (R(x))', color='green')
plt.plot(x, lucro_values, label='Lucro Total (P(x))', color='blue')

# Marcando o ponto ótimo
plt.scatter(ponto_otimo, lucro_otimo, color='orange', zorder=5)
plt.text(ponto_otimo, lucro_otimo, f' Ponto Ótimo: ({ponto_otimo:.2f}, {lucro_otimo:.2f})',
         horizontalalignment='right', fontsize=10)

# Configurando o gráfico
plt.title('Modelo de Produção: Custo, Receita e Lucro')
plt.xlabel('Quantidade Produzida (x)')
plt.ylabel('Valor (R$)')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.legend()
plt.grid()
plt.xlim(0, 10)
plt.ylim(-500, 1000)

# Exibindo o gráfico
plt.show()