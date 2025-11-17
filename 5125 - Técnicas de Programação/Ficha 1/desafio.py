print ("Desafio - Exercício 5 - While & For:")
print ("#######################")
print ("Desafio - Parte 1")
numinf = int( input ("Primeiro preciso que você me diga um número inferior à 15."))
while numinf >= 15:
    print ("Precisa ser inferior !!!")
    numinf = int( input ("Diz lá:"))
                  
numsup = int (input ("Primeiro preciso que você me diga um número superior à 30."))
while numsup <= 30:
    print ("Precisa ser superior !!!")
    numsup = int( input ("Diz lá:"))

contador = numinf
soma = 0

while contador <= numsup:
    soma = soma + contador
    contador = contador + 1
    print (soma)

print ("Agora vou fazer a mesma coisa com a Função For")

contador = numinf
soma = 0

for contador in range(numinf, numsup +1):
    soma += contador
    
print (f"Chegamos a conclusão que o intervalo de {numinf} à {numsup} é: {soma}.")

print ("#######################")
print ("Desafio - Parte 2")

print ("Agora faremos a multiplicação do intervalo dos números anteriores.")

contador2 = 0
mult = 0

while contador2 < numinf:
    mult = mult + numsup
    contador2 = contador2 + 1
    print (mult)

print (f"A multiplicação ficou em: {mult}")

print ("Agora vou fazer a mesma coisa com a Função For")

contador2 = numinf
mult = 0

for contador2 in range (0, numinf):
    mult=mult + numsup

print (f"A multiplicação ficou em: {mult}")

print ("#######################")
print ("Agora com funções:")

def pot_w(b,e):
    
    contador3 = 0
    conta = 0

    while contador3 < e:
        conta = b * b + conta
        contador3 = contador3 + 1
        


    return conta


