print ("Vamos trabalhar Fahrenheit para Celsius !")
print ("Vamos definir antes a fórmula utilizada.")
print ("Fahrenheit para Celsius (Insira 'F')")
print ("Celsius para Fahrenheit (Insira 'C')")

def obter_equa():
    equa =( input("Insira sua Conversão desejada:"))

    if equa == "F":
        fahr = float( input("Insira o valor em Fahrenheit:") )
        celsius = (fahr - 32)/1.8
        print (f"{fahr:.2f} Fahrenheit é igual à {celsius:.2f} Celsius.")

    elif equa == "C":
        celsius = float( input("Insira o valor em Celsius:") )
        fahr = (celsius*1.8) + 32
        print (f"{celsius:.2f} Celsius é igual à {fahr:.2f} Fahrenheit.")

    else :
        print ("Valor inválido")
        return obter_equa()

print ("=============================")

print ("E vamos ver seu IMC:")

c = float( input("Insira o valor da sua altura:") )

d = float( input("Agora Insira o valor do seu peso:") )

e = d/c**2

print (f"Seu IMC é {e:.2f}")
