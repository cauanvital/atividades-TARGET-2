import json

with open("dados.json") as file:fat = json.load(file)

loop = 0
val = 0
medqtd = 0
greval = [0, 0]
smaval = [0, fat[0]["valor"]]
dzero = []
dacim = []
acimed = 0

while loop < len(fat):
    # DEFINE OS VALORES PARA O CÁUCULO DA MÉDIA #
    if fat[loop]["valor"] == 0:
        val = val + fat[loop]["valor"]
        dzero.extend([fat[loop]["dia"]])
    else:
        val = val + fat[loop]["valor"]
        medqtd = medqtd + 1

    # DEFINE O VALOR MAIOR #
    if greval[1] <= fat[loop]["valor"]:
        greval[1] = fat[loop]["valor"]
        greval[0] = loop + 1

    # DEFINE O VALOR MENOR #
    if fat[loop]["valor"] != 0 and smaval[1] >= fat[loop]["valor"]:
        smaval[1] = fat[loop]["valor"]
        smaval[0] = fat[loop]["dia"]

    loop = loop + 1

loop = 0

finmed = val/medqtd

while loop < len(fat):
    if fat[loop]["valor"] > finmed:
        dacim.extend([fat[loop]["dia"]])

    loop = loop + 1

print("A média de lucro da empresa esse mês foi de {}".format(round(finmed, 4)))
print("Houveram {} dias com faturamento acima da média, sendo eles os dias {}".format(len(dacim), dacim))
print("O dia de maior faturamento foi o dia {}, com {} de lucro".format(greval[0], greval[1]))
print("Os dias menos lucrativos foram os dias {} sem nenhum faturamento".format(dzero))
print("sendo dia com menor faturamento acima de 0 foi o dia {}, com {} de lucro".format(smaval[0], smaval[1]))