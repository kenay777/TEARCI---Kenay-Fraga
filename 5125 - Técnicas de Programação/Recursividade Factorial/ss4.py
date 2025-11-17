##########################

def fact (n):
    if n==1:
        return (1)
    
    return (n*fact(n-1))

##########################

def mult (a,b):
    if a == 0:
        return 0
    if b == 1:
        return a

    return (a + mult(a,b-1))

##########################

def pot (base,expo):
    if base == 0:
        return 0
    
    if expo == 0:
        return 1

    if expo == 1:
        return base

    return (base*pot(base, expo-1))

##########################

def soma (inf,sup):

    if inf == sup:
        return inf

    return (inf+soma(inf+1, sup))

##########################

def fibonacci (mes):
    
    
    if mes == 0:
        return 0
    
    if mes == 1:
        return 1
    
    return (fibonacci(mes-1) + fibonacci (mes-2))

##########################

def caixas(cxa):
    if cxa == 0:
        return 0
    
    if cxa == 1:
        return 1
    
    return 2**caixas(cxa)+1

#2^caixa-1
