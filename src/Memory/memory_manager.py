from src.Memory.strategy import Strategy

class MemoryManager:
    '''Class representing a memory manager in SO'''
    strategy: Strategy = Strategy

    def __init__(self, strategy: Strategy):
        self.strategy = strategy
