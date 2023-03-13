#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ScrumMaster
import Integrante

class Equipo:
    def __init__(self, aId, aNombre, aSm):
        self.nombre = aNombre
        self.id = aId
        self.scrumMaster = aSm
        self.integrantes = []

    def getNombre(self):
        return self.nombre

    def setNombre(self, aNombre):
        self.nombre = aNombre

    def getId(self):
        return self.id

    def setId(self, aId):
        self.id = aId

    def addIntegrante(self, aIntegrante):
        self.integrantes.append(aIntegrante)

    def getScrumMaster(self):
        return self.scrumMaster

    def setScrumMaster(self, aScrumMaster):
        self.scrumMaster = aScrumMaster

    def __str__(self):
        return f"Equipo{{nombre={self.nombre}, id={self.id}, scrumMaster={self.scrumMaster}, integrantes={self.integrantes}}}"