# Importaçâo necessárias
from __future__ import annotations
from typing import Type

# Importações
from src.Memory.memory_manager import MemoryManager
from src.Memory.strategy import Strategy
from src.CPU.cpu_manager import CpuManager
from src.Schedule.schedule import Schedule
from src.SO.system_call_type import SystemCallType
from src.SO.process import Process

class SystemOperation:
    '''Class representing a system operation'''

    _mm: MemoryManager = None
    _cm: CpuManager = None
    _schedule: Schedule = None

    # Getters and setters
    @property
    def mm(self) -> MemoryManager:
        return self._mm
    
    @mm.setter
    def mm(self, value: MemoryManager) -> None:
        self._mm = value

    @property
    def cm(self) -> CpuManager:
        return self._cm
    
    @cm.setter
    def cm(self, value: CpuManager) -> None:
        self._cm = value
    
    @property
    def schedule(self) -> Schedule:
        return self._schedule

    @schedule.setter
    def schedule(self, value: Schedule) -> None:
        self._schedule = value

    # Métodos
    def system_call(self, call_type: SystemCallType, p: Process) -> object:
        if call_type == SystemCallType.WRITE_PROCESS:
            # Escrever
            pass
        elif call_type == SystemCallType.CREATE_PROCESS:
            # Criar
            if _cm is None:
                _cm = CpuManager()
            if _mm is None:
                _mm = MemoryManager(Strategy.FIRST_FIT)

            return Process()

        elif (call_type == SystemCallType.DELETE_PROCESS):
            # Apagar
            pass
        elif (call_type == SystemCallType.READ_PROCESS):
            # Leitura
            pass
        else:
            raise Exception('Invalid system call type')

        return None
