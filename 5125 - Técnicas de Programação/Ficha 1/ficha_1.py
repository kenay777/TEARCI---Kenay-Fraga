print ("Vamos realizar a ficha 1")

print ("########################")

print ("Exercício 1 : a = 1")

a=5
print (a)

print ("Exercício 1 : a = 7")

b=7
print (b)

print ("Exercício 1 : a + b")

c=a+b
print (c)

print ("########################")

print ("Exercício 2 - Perguntas ao utilizador & Circunstâncias:")

idade = int(input("Diga a sua idade, por favor."))

if idade > 0 :
        print ("Sua idade é maior que zero !")

elif idade < 0 :
    print ("Sua idade e menor que zero !")
    
print ("########################")

print ("Exercício 3 - Número de Km's & Gasto Médio do Carro:")

km = int (input ("Quantos Quilômetros seu carro já viajou ?"))

litros = int (input("Quantos litros seu carro consome à cada 100km ?"))

litrosconsu = km//litros

litroseuro =round(litrosconsu * 1.75,2)

print (f"Seu carro consumiu {litrosconsu}, com o valor de {litroseuro} €.")

print ("########################")

print ("Exercício 4 - Cálculo de IMC:")

altura = float(input("Diga a sua altura, por favor."))

peso = float(input("Diga seu peso, por favor."))

imc = peso/altura**2

if imc < 18.5:
    print ("Seu IMC é menor que 18,5/m2 - Está abaixo do peso.")

if imc >= 18.5 and imc <= 25:
    print (f"Seu IMC é {imc:.2f} e está adequado.")
    
if imc >=25 and imc <= 30:
    print (f"Seu IMC é {imc:.2f} e está em sobrepeso.")

if imc >30:
    print (f"Seu IMC é {imc:.2f} e está em obesidade.")
 


