class AddressMemory:
    ''' Class for representing an address in memory '''
    _start: int = None
    _end: int = None

    def __init__(self, start: int, end: int):
        self._start = start
        self._end = end

    # Methods
    def size(self) -> int:
        return (self._end - self._start) + 1

    # Getters and Setters
    @property
    def start(self) -> int:
        return self._start

    @property
    def end(self) -> int:
        return self._end

    @start.setter
    def start(self, value: int):
        self._start = value

    @end.setter
    def end(self, value: int):
        self._end = value
