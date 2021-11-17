
class Usuario(object):
    """
    Author: Victor Calzada
    Date: 08/10/2021

    Clase usuario para manejar los ejercicios que ejecuta
    """


    def __init__(self, nombre, peso, altura):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def updatePeso(self, peso):
        """
        Actualiza el peso del usiario
        Argumentos:
        -float peso
        """
        self.peso = peso

    def updateAltura(self, altura):
        """
        Actualiza la altura del usiario
        Argumentos:
        -float peso
        """
        self.altura = altura

    def planDeEntreno(self, plan):
        """
        Establece un plan de entreno entre los posibles planes previstos
        Argumentos:
        -string plan
        """
        self.plan = plan