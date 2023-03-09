sta = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}
soma = sum(sta.values())

for i in sta.keys():
    per = sta[i] * 100 / soma
    print(f'{i} é responsável por {round(per, 1)}% do faturamento da distribuidora')

print("Valores arredondados.")
