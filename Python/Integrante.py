#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Equipo
from typing import List

class Integrante(object):
	def getNombre(self) -> String:
		return self.__nombre

	def setNombre(self, aNombre : String) -> None:
		self.__nombre = aNombre

	def getRol(self) -> String:
		return self.__rol

	def setRol(self, aRol : String) -> None:
		self.__rol = aRol

	def toString(self):
		pass

	def Integrante(self, aNombre : String, aRol : String):
		pass

	def __init__(self):
		self.__nombre : String = None
		self.__rol : String = None
		self.equipo : Equipo = None
		"""# @AssociationMultiplicity 1"""
		self.tareas = []
		"""# @AssociationMultiplicity *
		# @AssociationKind Aggregation"""

