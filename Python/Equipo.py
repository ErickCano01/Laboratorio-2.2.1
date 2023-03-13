#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ScrumMaster
import Integrante
from typing import List

class Equipo(object):
	def getNombre(self) -> String:
		return self.__nombre

	def setNombre(self, aNombre : String) -> None:
		self.__nombre = aNombre

	def getId(self) -> int:
		return self.__id

	def setId(self, aId : int) -> None:
		self.__id = aId

	def addIntegrate(self, aIntegrante : Integrante):
		pass

	def toString(self):
		pass

	def getScrumMaster(self) -> ScrumMaster:
		return self.scrumMaster

	def setScrumMaster(self, aScrumMaster : ScrumMaster) -> None:
		self.scrumMaster = aScrumMaster

	def Equipo(self, aId : int, aNombre : String, aSm : ScrumMaster):
		pass

	def __init__(self):
		self.__nombre : String = None
		self.__id : int = None
		self.__scrumMaster : ScrumMaster = None
		self.integrantes = []
		"""# @AssociationMultiplicity *
		# @AssociationKind Aggregation"""

