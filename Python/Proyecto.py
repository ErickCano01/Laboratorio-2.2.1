#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List
class Proyecto:
    def __init__(self, nombre, fechaInicio, estado):
        self.nombre = nombre
        self.fechaInicio = fechaInicio
        self.estado = estado
        self.equipos = []
        self.stakeholders = []
        self.tareas = []

    def getNombre(self):
        return self.nombre

    def setNombre(self, aNombre):
        self.nombre = aNombre

    def getFechaInicio(self):
        return self.fechaInicio

    def setFechaInicio(self, aFechaInicio):
        self.fechaInicio = aFechaInicio

    def getEstado(self):
        return self.estado

    def setEstado(self, aEstado):
        self.estado = aEstado

    def __str__(self):
        sb = []
        sb.append("Proyecto{")
        sb.append("nombre=" + self.nombre)
        sb.append(", fechaInicio=" + self.fechaInicio)
        sb.append(", estado=" + str(self.estado))
        sb.append(", equipos=" + str(self.equipos))
        sb.append(", stakeholders=" + str(self.stakeholders))
        sb.append(", tareas=" + str(self.tareas))
        sb.append('}')
        return ''.join(sb)
