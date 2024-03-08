from enum import Enum, auto

class Strategy(Enum):
    ''' Algorithm for SO '''
    BEST_FIT = auto()
    WORST_FIT = auto()
    FIRST_FIT = auto()
    PAGING = auto()
