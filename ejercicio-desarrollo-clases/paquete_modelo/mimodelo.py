#Creamos la clase Persona
class Persona(object):
    #Creamos el constructor que recibe el nombre y 3 notas 
    def __init__(self, n, n1, n2, n3):
        self.nombre = n
        self.nota1 = float(n1)
        self.nota2 = float(n2)
        self.nota3 = float(n3)

    #Metodos de agregar y obtener de los atributos
    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_nota1(self, n1):
        self.nota1 = float(n1)

    def obtener_nota1(self):
        return self.nota1
    
    def agregar_nota2(self, n2):
        self.nota2 = float(n2)

    def obtener_nota2(self):
        return self.nota2

    def agregar_nota3(self, n3):
        self.nota3 = float(n3)

    def obtener_nota3(self):
        return self.nota3

    #Metodo para calcular el promedio
    def calculo_promedio(self):#Calculamos el promedio sumando las 3 notas y dividiendo para 3
        return (self.nota1 + self.nota2 + self.nota3) / 3
    
    #Metodo str para presentar los datos con el Nombre y el promedio calculado
    def __str__(self):
        return "\nNombre: %s - Promedio: %f" % (self.nombre, self.calculo_promedio())