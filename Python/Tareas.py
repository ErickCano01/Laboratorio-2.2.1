#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Integrante
from typing import List

class Tareas(object):
	def getContexto(self):
		pass

	def setContexto(self, aContexto) -> None:
		pass

	def getId(self) -> int:
		return self.__id

	def setId(self, aId : int) -> None:
		self.__id = aId

	def getPrioridad(self) -> int:
		return self.__prioridad

	def setPrioridad(self, aPrioridad : int) -> None:
		self.__prioridad = aPrioridad

	def __init__(self):
		self.__id : int = None
		self.__prioridad : int = None
		self.__contexto : String = None
		self.encargado : Integrante = None
		"""# @AssociationMultiplicity 1"""

