from enum import Enum, auto

class SystemCallType(Enum):
    '''Enum for system call types'''
    CREATE_PROCESS = auto()
    READ_PROCESS = auto()
    WRITE_PROCESS = auto()
    DELETE_PROCESS = auto()
