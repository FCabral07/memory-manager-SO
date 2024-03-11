from src.SO.process import Process
from src.SO.system_operation import SystemOperation
from src.SO.system_call_type import SystemCallType
from src.Memory.memory_manager import MemoryManager

if __name__ == "__main__":
    operation = SystemOperation()
    p1 = operation.system_call(SystemCallType.CREATE_PROCESS, None)
    operation.system_call(SystemCallType.WRITE_PROCESS, p1)

    # p2 = operation.system_call(SystemCallType.CREATE_PROCESS, None)
    # operation.system_call(SystemCallType.WRITE_PROCESS, p2)

    # p3 = operation.system_call(SystemCallType.CREATE_PROCESS, None)
    # operation.system_call(SystemCallType.WRITE_PROCESS, p3)

    # p4 = operation.system_call(SystemCallType.CREATE_PROCESS, None)
    # operation.system_call(SystemCallType.WRITE_PROCESS, p4)

    # memory = operation.return_memory()

    # operation.system_call(SystemCallType.DELETE_PROCESS, p3)

    # p5 = operation.system_call(SystemCallType.CREATE_PROCESS, None)
    # operation.system_call(SystemCallType.WRITE_PROCESS, p5)

    # p6 = operation.system_call(SystemCallType.CREATE_PROCESS, None)
    # operation.system_call(SystemCallType.WRITE_PROCESS, p6)

    memory = operation.return_memory()
