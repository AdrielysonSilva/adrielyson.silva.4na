# 1. Definir as listas x e y
listax = [1, 3, 4, 5]
listay = [7, 8, 9, 10]
# 2. Calcular as médias de x e y
mediax = sum(listax)/len(listax)
mediay = sum(listay)/len(listay)

# 3. Inicializar as variáveis para os somatórios
somaxy = 0
somax2 = 0
# 4. Utilizar um loop para calcular:
#    - A soma de (x_i - média_x) * (y_i - média_y)
#    - A soma de (x_i - média_x)²
for c in range(len(listax)):
    xi = listax[c]
    yi = listay[c]

    somaxy += (xi-mediax)*(yi-mediay)
    somax2 += (xi - mediax) ** 2
# 5. Calcular beta1 e beta0 usando as fórmulas dos mínimos quadrados
#beta1 = intercepto
#beta0 = inclinação
beta1 = somaxy / somax2 
beta0 = mediay - beta1 *mediax  
# 6. Imprimir os resultados
print(f"Equação da reta y = {beta1}x + {beta0}")