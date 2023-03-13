#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Equipo
from typing import List

class ScrumMaster(object):
	def getNombre(self) -> String:
		return self.__nombre

	def setNombre(self, aNombre : String) -> None:
		self.__nombre = aNombre

	def getRolSecundario(self) -> String:
		return self.__rolSecundario

	def setRolSecundario(self, aRolSecundario : String) -> None:
		self.__rolSecundario = aRolSecundario

	def ScrumMaster(self, aNombre : String, aRolSecundario : String):
		pass

	def __init__(self):
		self.__nombre : String = None
		self.__rolSecundario : String = None
		self.hasA : Equipo = None
		"""# @AssociationMultiplicity 1"""

