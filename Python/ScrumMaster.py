#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Equipo
from typing import List

class ScrumMaster:

    def __init__(self, nombre):
        self.nombre = nombre
        self.rolSecundario = ""

    def getNombre(self):
        return self.nombre

    def setNombre(self, aNombre):
        self.nombre = aNombre

    def getRolSecundario(self):
        return self.rolSecundario

    def setRolSecundario(self, aRolSecundario):
        self.rolSecundario = aRolSecundario

    def __str__(self):
        return f"ScrumMaster{{nombre={self.nombre}, rolSecundario={self.rolSecundario}}}"
