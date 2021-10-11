from __future__ import annotations

class Usuario(object):
    """
    Author: Victor Calzada
    Date: 08/10/2021

    Clase usuario para manejar los ejercicios que ejecuta
    """


    def __init__(self, str: nombre, float: peso, float: altura) -> void:
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def updatePeso(self, float: peso) -> void:
        """
        Actualiza el peso del usiario
        Argumentos:
        -float peso
        """
        self.peso = peso

    def updateAltura(self, float: altura) -> void:
        """
        Actualiza la altura del usiario
        Argumentos:
        -float peso
        """
        self.altura = altura
