n1 = 0
n2 = 1
n3 = 0
i = int(input("Digite um número inteiro:"))

while i > n3:
  n3 = n1 + n2
  n1 = n2
  n2 = n3

if i == 0:
  print("{} faz parte da sequência de Fibonacci!".format(i))
elif i == n3:
  print("{} faz parte da sequência de Fibonacci!".format(i))
else:
  print("{} não faz parte da sequência de Fibonacci!".format(i))

