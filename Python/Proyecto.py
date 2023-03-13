#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class Proyecto(object):
	def getNombre(self) -> String:
		return self.__nombre

	def setNombre(self, aNombre : String) -> None:
		self.__nombre = aNombre

	def getFechaInicio(self) -> String:
		return self.__fechaInicio

	def setFechaInicio(self, aFechaInicio : String) -> None:
		self.__fechaInicio = aFechaInicio

	def getEstado(self) -> Boolean:
		return self.__estado

	def setEstado(self, aEstado : Boolean) -> None:
		self.__estado = aEstado

	def __init__(self):
		self.__nombre : String = None
		self.__fechaInicio : String = None
		self.__estado : Boolean = None
		self.equipos = []
		"""# @AssociationMultiplicity *
		# @AssociationKind Aggregation"""
		self.stakeholders = []
		"""# @AssociationMultiplicity *
		# @AssociationKind Aggregation"""
		self.tareas = []
		"""# @AssociationMultiplicity *
		# @AssociationKind Aggregation"""

