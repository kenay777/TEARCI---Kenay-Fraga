# i=0
# soma=0
# enquanto i<=100
# soma=soma+i
# i=i+1
print ("Prepare-se pro contador !!!")
i=0

while (i <= 100) :
    print (i)
    i = i + 1
    
print ("===================================")
print ("Vamos falar da páscoa !!!")
ANO = int(input ("Diga-me o ano ! "))

x = 24
y = 5
a = ANO % 19
b = ANO % 4
c = ANO % 7
d = ((19*a)+x)% 30
e = ((2*b)+(4*c)+(6*d)+y)% 7

if (d+e)<10 :
    dia=(d+e+22)
    print(dia,"de Março.")

else :
    dia=(d+e-9)
    print(dia,"de Abril.")
    
print ("===================================")
print ("Vamos trabalhar com a curiosidade !")
print ("Diga-me um ano e vamos ver se ele é bissexto ou não !")

i = int(input("Diga o ano à vontade: "))

if (i % 4 == 0 and i % 100 != 0 ) or i % 400 == 0:
    print ("O ano",i,"é bissexto !!!")

else :
    print ("O ano",i,"não é bissexto !!!")
