def validar_isbn(isbn):

    if len(isbn) != 13 : #Verificar tamanho
            print ("ISBN Inválido !")
            return False
    
    if not isbn.isdigit():
        print ("ISBN Inválido !")
        return False    
 
    soma = 0
    
    for i in range(len(isbn)):
        numero = int(isbn[i])
        if i % 2 == 0: 
            soma += numero
        else: 
            soma += numero * 3
            
    resto = soma % 10

    if resto == 0:
        print ("Número válido !")

    else:
        print ("Número inválido !")
