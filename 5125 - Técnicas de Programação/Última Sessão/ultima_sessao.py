def par(x):

    if x%2==0:
        print (x,"é par.")

    else:
        print (x,"é ímpar.")
    
def semaforo(nome):

    if "Vermelho" in nome:
        print ("Passagem proíbida.")
        
    elif "Amarelo" in nome:
        print ("Transição para amarelo.")
        
    elif "Verde" in nome:
        print ("Passagem permitida.")   
    else:
        print ("Cor Inválida")

def fatorial_w(fact):
    
    n = fact - 1

    while i > 0 :       
        fact = fact * n
        n = n - 1

    return fact


def fatorial_f(fact):
    
    n = fact - 1

    for n in range (1, fact):       
        fact = fact * n
        n = n - 1

    return fact

def fatorial_r(n):

    if n==1:
        return (1)
    
    return (n*fatorial_r(n-1))

def teste_lista():
    
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    soma = 0
    contador = 0
    for i in lista:
        soma += i
        contador += 1

    media = soma/contador
    
    print ("A soma de todos é", soma)
    print ("A soma de todos é", media)


def teste_NIF(nif):

    if len(nif) != 9 :
        print ("NIF inválido")
        return False

    for i in nif:
        if i.isalpha():
            print ("NIF inválido")
            return False
        
    soma = 0
    teste = 9
    
    for i in range(8):
        soma += int(nif[i]) * teste
        teste = teste - 1  

    resto = soma%11
    
    if resto == 0:
        print ("NIF Válido")
        
    elif resto == 1:
        print ("NIF Válido")

    else:
        print ("NIF Inválido")
    

