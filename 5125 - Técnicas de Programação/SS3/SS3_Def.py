def par(x):
    if x % 2 == 0:
        return ("Par")

    else:
        return ("Ímpar")

def pos(x):
    if x<0 :
        return ("Negativo")
    if x==0:
        return ("Zero ;D")
    if x>0:
        return ("Positivo")

def ven(totobola1,totobola2):
    if totobola1<totobola2 :
        return ("Totobola 2 Ganhou.")
    if totobola1>totobola2:
        return ("Totobola 1 Ganhou.")
    else:
        return ("Empate Totobola.")

def pasc(ANO):
    
    x = 24
    y = 5
    a = ANO % 19
    b = ANO % 4
    c = ANO % 7
    d = ((19*a)+x)% 30
    e = ((2*b)+(4*c)+(6*d)+y)% 7

    if (d+e)<10 :
        dia=(d+e+22)
        return(dia,"de Março.")
                
    else :
        dia=(d+e-9)
        return(dia,"de Abril.")

def bi(i):
    if (i % 4 == 0 and i % 100 != 0 ) or i % 400 == 0:
        return ("O ano",i,"é bissexto !!!")

    else :
        return ("O ano",i,"não é bissexto !!!")

def imc(c,d):
    e = d/c**2
    return ("Seu IMC é:",e)

def cel(x):
    far=(x*1.8)+32
    return (x,"Celsius em Fahrenheint é equivalente à:",far,"Fahrenreint.")

def far(x):
    cel=(x - 32)/1.8
    return (x,"Fahrenreint em Celsius é equivalente à:",cel,"Celsius.")


def fato(x):
    i=x-1
    
    for i in range (i,0,-1):
        x = x*i
        i = i-1

    return (x)
