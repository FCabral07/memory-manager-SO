from enum import Enum, auto

class Strategy(Enum):
    ''' Algorithm for SO '''
    FIRST_FIT = auto()
    BEST_FIT = auto()
    WORST_FIT = auto()
    PAGING = auto()
