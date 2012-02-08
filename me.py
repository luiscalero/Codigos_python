import math

def factorial_numero(n):
    a=1
    if n<0:
        return 0
    elif n==0:
        return 0
    else:
        for i in range(2,n+1):
            a=a*i
        return "El factorial es",a
    

def numero_primo(numero):
    num=numero
    creo_que_es_primo = 1
    for divisor in range(2, num):
        if num % divisor == 0:
         creo_que_es_primo = 0
    if creo_que_es_primo:
       print  num, "es primo "
    else:
       print  num, "no es primo" 

def palindroma(c):
    cadena = c
    if(cadena==cadena[::-1]):
      print cadena,"es palindroma"
    else:
      print cadena,"no es palindroma"
      
  
def raiz(n):
     raiz=math.sqrt(n)
     print "La raiz es : ",raiz








