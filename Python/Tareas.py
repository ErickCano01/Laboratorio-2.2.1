#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Integrante
from typing import List

def __init__(self, id, prioridad, contexto, encargado):
    self.id = id
    self.prioridad = prioridad
    self.contexto = contexto
    self.encargado = encargado

def get_contexto(self):
    raise NotImplementedError()

def set_contexto(self, contexto):
    raise NotImplementedError()

def get_id(self):
    return self.id

def set_id(self, id):
    self.id = id

def get_prioridad(self):
    return self.prioridad

def set_prioridad(self, prioridad):
    self.prioridad = prioridad

def set_contexto(self, contexto):
    self.contexto = contexto

def __str__(self):
    return f"Tareas{{id={self.id}, prioridad={self.prioridad}, contexto={self.contexto}, encargado={self.encargado}}}"
