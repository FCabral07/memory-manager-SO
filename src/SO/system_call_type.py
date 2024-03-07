from enum import Enum, auto

class SystemCallType(Enum):
    '''Enum for system call types'''
    WRITE_PROCESS = auto()
    DELETE_PROCESS = auto()
    READ_PROCESS = auto()
    CREATE_PROCESS = auto()
