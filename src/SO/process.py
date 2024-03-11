from __future__ import annotations # Importação para chamar o próprio process dentro dele e tipar a lista
from typing import Type, List # Importação para tipar
import uuid # id aleatório
import random # Gera coisas aleatórias

from ..Memory.address_memory import AddressMemory

class Process:
    '''Class representing a process in SO'''
    # Definindo um array para tamanhos específicos do processo na memória
    _rand_size: List[int] = [1, 2, 4, 5, 8, 10, 20, 50, 100]
    _uid: str = None
    _size_in_memory: int = None
    # _process: List[Process] = None
    # _time_to_execute: int = None
    _address_in_memory: AddressMemory = None

    def __init__(self):
        # Definindo randomicamente o id do processo e o tamanho ocupado na memória
        self._uid = str(uuid.uuid4())
        self._size_in_memory = random.choice(self._rand_size)
        print(f"Processo criado: UID={self._uid}, Tamanho na Memória={self._size_in_memory}")

    # Getters and setters
    @property
    def uid(self) -> str:
        return self._uid

    @property
    def size_in_memory(self) -> int:
        return self._size_in_memory
    
    @uid.setter
    def uid(self, value: str):
        self._uid = value

    @size_in_memory.setter
    def size_in_memory(self, value: int):
        self._size_in_memory = value
