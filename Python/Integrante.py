#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Equipo

class Integrante:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
        self.tareas = []

    def getNombre(self):
        return self.nombre

    def setNombre(self, aNombre):
        self.nombre = aNombre

    def getRol(self):
        return self.rol

    def setRol(self, aRol):
        self.rol = aRol

    def __str__(self):
        return "Integrante{nombre=" + self.nombre + ", rol=" + self.rol + ", tareas=" + str(self.tareas) + "}"