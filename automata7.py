import random as rand
Lenguaje=["0","1"]
palindrome=list()
def CreaArchivo():
    archi1=open("ListaPalindrome.txt",'w')
    archi1.close()
def escribirArchivo(cadena):
    archi=open("ListaPalindrome.txt",'a')
    archi.write(cadena)
    archi.close()
def GenerarCadena(cantidad):
    '''random number generator'''
    if(cantidad%2==1):
        print(cantidad)
        qty=cantidad-1
        palindrome.append("e")
        R1(0,"".join(palindrome))
        qty=qty/2
        for i in range (int(qty)):
            entrada=rand.choice(Lenguaje)
            palindrome.append(entrada)
            if(entrada=="0"):
                R2(i+1,"".join(palindrome))
            else:
                R3(i+1,"".join(palindrome))
    else:
        qty=cantidad/2
        for i in range (int(qty)):
            entrada=rand.choice(Lenguaje)
            palindrome.append(entrada)
            if(entrada=="0"):
                R2(i+1,"".join(palindrome))
            else:
                R3(i+1,"".join(palindrome))
    print("".join(palindrome))
    return "".join(palindrome)
    
    
'''Reglas de produccion:
(1) P -> e
(2) P -> 0
(3) P -> 1
(4) P -> 0P0
(5) P -> 1P1
'''
def R1(indice,cadena):
    escribirArchivo("P->e |"+str(indice)+" str:"+cadena+"\n") 
def R2(indice,cadena):
    escribirArchivo("P->0 |"+str(indice)+" str:"+cadena+"\n")
def R3(indice,cadena):
    escribirArchivo("P->1 |"+str(indice)+" str:"+cadena+"\n")
def R4(indice,cadena):
    escribirArchivo("P->0P0 |"+str(indice)+" str:"+cadena+"\n")
def R5(indice,cadena):
    escribirArchivo("P->1P1 |"+str(indice)+" str:"+cadena+"\n")
    
'''Funcion espejo: Refleja lo visto en la cadena para de esta manera crear el palindromo'''
def MirrorForce(cadena):
    for item in cadena[::-1]:
        if(item=="0"):
            palindrome.append("0")
            R4(len(palindrome),"".join(palindrome))
        elif(item=="1"):
            palindrome.append("1")
            R5(len(palindrome),"".join(palindrome))
    print("".join(palindrome))
CreaArchivo()
selec=0
while(selec!=3):
    print("Bienvenido al generador de palindrome, seleccione una de las siguientes opciones para continuar:\n1-Insertar Longitud\n2-Longitud Aleatoria\n3-Salir")
    selec=input("Ingresa la opcion elegida:")
    if(selec=="1"):
        CreaArchivo()
        print("Ingrese la longitud del palindromo:")
        qty=input()
        if(int(qty)<=100000):
            cadena=GenerarCadena(int(qty))
            MirrorForce(list(cadena))
        else:
            print("Error la longitud es mayor a 100000")
    elif(selec=="2"):
        CreaArchivo()
        cantidadAleatoria=rand.randint(0,100000)
        cadena=GenerarCadena(cantidadAleatoria)
        MirrorForce(list(cadena))
    elif(selec=="3"):
        exit()
    else:
        print("Error. Opcion no valida")