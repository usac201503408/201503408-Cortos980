n=2 #inicializacion de variable con la que se trabajara
contador=2 #contador de iteraciones
while (contador<=408): #mientras no se llege a 408, seguira realizando iteraciones
    collatz=[]
    n=contador #se iguala la variable que se trabajara al contador para iniciar el proceso
    collatz.append(n)
    
    while (n > 1): #algoritmo de collatz termina cuando n deja de ser mayor que 1
        if (n%2==0):
                n=n//2
        else:
            n= (3*n)+1
        
        collatz.append(n)#agrega los elementos de la secuencia de collatz a una lista llamada collatz
    print(collatz)
    contador+=1