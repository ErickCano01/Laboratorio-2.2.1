#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class Stakeholder:

    def __init__(self, presupuesto, nombre, id):
        self.presupuesto = presupuesto
        self.nombre = nombre
        self.id = id

    def get_presupuesto(self):
        return self.presupuesto

    def set_presupuesto(self, presupuesto):
        self.presupuesto = presupuesto

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return f"Stakeholder{{presupuesto={self.presupuesto}, nombre={self.nombre}, id={self.id}}}"
