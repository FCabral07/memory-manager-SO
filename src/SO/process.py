from __future__ import annotations # Importação para chamar o próprio process dentro dele e tipar a lista
from typing import Type, List # Importação para tipar
import uuid # id aleatório
import random # Gera coisas aleatórias

from ..Memory.address_memory import AddressMemory

class Process:
    '''Class representing a process in SO'''
    
    _uid: str = str(uuid.uuid4())
    _size_in_memory: int = None
    # _process: List[Process] = None
    # _time_to_execute: int = None
    _address_in_memory: AddressMemory = None

    # Getters and setters
    @property
    def uid(self) -> str:
        return self._uid

    @property
    def address_in_memory(self) -> AddressMemory:
        return self._address_in_memory

    @property
    def size_in_memory(self) -> int:
        return self._size_in_memory
    
    @uid.setter
    def uid(self, value: str):
        self._uid = value

    @size_in_memory.setter
    def size_in_memory(self, value: int):
        self._size_in_memory = value
    
    @address_in_memory.setter
    def address_in_memory(self, value: AddressMemory):
        self._address_in_memory = value
