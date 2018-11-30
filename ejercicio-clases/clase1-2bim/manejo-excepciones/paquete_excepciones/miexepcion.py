"""
    Manejo de Excepciones
"""

class MiError(Exception):
    """
    """

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "Existe un error para%s" %(self.valor)
