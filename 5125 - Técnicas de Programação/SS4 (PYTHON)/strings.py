def validar_nome(nome):

    for i in nome: #Letra no Nome
        if i >="0" and i <="9":
            print ("Nome Inválido !")
            return False
        
    if len(nome) < 6 : #Nome pequeno
        print ("Nome Inválido !")
        return False

    ind=nome.find(' ') #Procurar espaço
    if ind == -1:
        print ("Nome Inválido !")
        return False
    
    print ("Nome Válido !") #Conclusão
    return True




def validar_email(email):
    # Verifica se termina com "@formacao.iefp.pt"
    if not email.endswith("@formacao.iefp.pt"):
        print("Nome Inválido!")
        return False
    
    # Verifica espaço
    if " " in email:
        print("O email não pode conter espaços.")
        return False
    
    # Verifica letra maiúscula
    if any(letra.isupper() for letra in email):
        print("O email não pode conter letras maiúsculas.")
        return False
    
    print("Tudo Ok")
    return True  # Retorna True se for válido

