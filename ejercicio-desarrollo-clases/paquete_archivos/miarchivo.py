import codecs#Importamos el codecs

class MiArchivo:#Creamos la clase Mi archivo para leer el archivo
    #Constructor de la clase
    def __init__(self):
        self.archivo = codecs.open("data/informacion.csv", "r")#Colocamos la dirección del archivo que contiene la informacion

    #Metodos de leer informacion
    def obtener_informacion(self):
        return self.archivo.readlines()

    #Metodo para cerrar el archivo
    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:#Creamos la clase para escribir en mi archivo
    #Constructor de la clase
    def __init__(self):
        self.archivo = codecs.open("data/informacion2.csv", "a")#Colocamos la dirección del archivo en el cual escribiremos 

    #Metodo para escribir informacion en el archivo informacion2
    def agregar_informacion(self, p):
        self.archivo.write("Nombre: %s - Promedio: %f\n" % (p.nombre, p.calculo_promedio()))

    #Metodo para cerrar el archivo
    def cerrar_archivo(self):
        self.archivo.close()
