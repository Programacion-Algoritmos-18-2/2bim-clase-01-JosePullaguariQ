#Importamos las clases que utilizaremos
from paquete_archivos.miarchivo import MiArchivo, MiArchivoEscribir
from paquete_modelo.mimodelo import Persona

#Creamos el objeto m de tipo Mi Archivo
m = MiArchivo()
#Creamos el objeto m2 de tipo Mi Archivo Escribir
m2 = MiArchivoEscribir()

#Creamos la lista y separamos con el split
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

#Inicializamos la lista en la posicion 1
lista = lista[1:]

#Recorremos la lista con un for mejorado
for d in lista:
    p = Persona(d[0], d[1], d[2], d[3]) #Enviamos al objeto tipo persona los elementos en la posicio 0 1 2 3
    print(p)							#Presentamos el objeto p
    m2.agregar_informacion(p)			#Agregamos la información al objeto m2 que es tipo Mi Archivo Escribir

#Cerramos el archivo con los objetos creados
m.cerrar_archivo()
m2.cerrar_archivo()
