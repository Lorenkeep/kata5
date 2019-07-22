import os

def valida(valor):
    valido = False
    while valido == False:
        try:
            valor=int(valor)
            if valor >0:
                valido = True
            else:
                print ("El valor introducion es incorrecto.\n Introduce un numero valido")
                valor = input("Introduce el registro a borrar: ")
        except:
            valor = input("Introduce el registro a borrar: ")
    return int(valor)

ficheroentrada = open('movimientos.txt' , 'r')
ficherossalida = open('nuevomovimientos.txt' , 'w')
log = open("log.txt", "a+")
ix = input("Registro a borrar")
ix = valida(ix)


#Montar proceso que vaya leyendo y copiando de movimientos.txt a nuevomovimientos.txt excepto el registro elegido
#Despues, borrar movimientos y renombrar nuevomovimientos a movimientos

linea = ficheroentrada.readline()
leelinea = 1


while linea != "":
    
    if ix <=0:
        print ("Introduce un número de registro correcto")
        ix = input("Registro a borrar")
        ix = int(ix)
        leelinea = 1

    elif ix == leelinea:
        log.write(linea)
        linea = ficheroentrada.readline()
        leelinea +=1

    else:
        ficherossalida.write(linea)
        linea = ficheroentrada.readline()
        leelinea +=1

if len(linea) < leelinea:
    print ("Ese numero de registro no existe")
    ix = input("Introduce el registro a borrar")

ficheroentrada.close()
ficherossalida.close()
log.close()

os.remove("movimientos.txt")
os.rename("nuevomovimientos.txt","movimientos.txt")
#os.replace("nuevomovimientos.txt" , "movimientos.txt") ESTO ERA UNA PRUEBA

#falta validar las entrada si no es un numero ¿probamos con un try except?
#falta validar si el numero de registro dado en el input es mayor que el numero de lineas de movimientos.txt

#faltará hacer la funcionalidad de "DESHACER" haciendo que la ultima linea del log, lo ponga en movimientos.txt
