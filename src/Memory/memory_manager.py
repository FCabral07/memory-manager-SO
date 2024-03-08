from src.Memory.strategy import Strategy
from ..SO.process import Process

class MemoryManager:
    '''Class representing a memory manager in SO'''
    strategy: Strategy = Strategy

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def write(self) -> None:
        if self.strategy == Strategy.FIRST_FIT:
            # TODO implement strategy
            pass
