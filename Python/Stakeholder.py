#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class Stakeholder(object):
	def getPresupuesto(self) -> float:
		return self.__presupuesto

	def setPresupuesto(self, aPresupuesto : float) -> None:
		self.__presupuesto = aPresupuesto

	def getNombre(self) -> String:
		return self.__nombre

	def setNombre(self, aNombre : String) -> None:
		self.__nombre = aNombre

	def getId(self) -> int:
		return self.__id

	def setId(self, aId : int) -> None:
		self.__id = aId

	def __init__(self):
		self.__presupuesto : float = None
		self.__nombre : String = None
		self.__id : int = None

