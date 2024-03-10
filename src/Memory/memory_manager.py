from typing import List, Type

from src.Memory.strategy import Strategy
from src.SO.process import Process
from src.Memory.address_memory import AddressMemory

class MemoryManager:
    ''' Class representing a memory manager in SO '''
    _strategy: Strategy = None
    _physical_memory: List[str] = None
    # Caso use paginação -> Logical memory
    

    def __init__(self, strategy: Strategy):
        self._strategy = strategy
        self._physical_memory: List[str] = [None] * 128
        # Mapeando o processo para printar ao invés do código
        self._process_map = {}
        self._process_counter = 1

    def write(self, p: Process) -> None:
        ''' Selector method for choice what kind of algorithm to use '''
        if self._strategy == Strategy.FIRST_FIT:
            self.write_using_first_fit(p)
        elif self._strategy == Strategy.BEST_FIT:
            self.write_using_best_fit(p)
        elif self._strategy == Strategy.WORST_FIT:
            self.write_using_worst_fit(p)
        # elif self._strategy == Strategy.PAGING:
            # self.write_using_paging(p)
    
    def delete(self, p: Process) -> None:
        ''' Method for delete a process from the memory '''
        for i, uuid in enumerate(self._physical_memory):
            if uuid == p.uid:
                self._physical_memory[i] = None
                
        self._process_map.pop(p.uid)
                

    def write_using_first_fit(self, p: Process) -> None:
        ''' Method for write a process using first fit '''
        actual_size = 0  # Tamanho atual do espaço disponível na memória
        start = 0        # Define onde é o início do espaço a ser salvo o processo
                         # onde a memória é livre

        # Usando enumerate para percorrer a memória
        for i, block in enumerate(self._physical_memory):
            if block is None:
                # Se o valor em i for None, ou seja, estiver vazio, entra no bloco
                if actual_size == 0:
                    # Verifica se o actual size é 0, caso seja, indica que é o 
                    # início de um espaço vazio e define o start para o espaço i
                    start = i
                actual_size += 1
                if actual_size >= p.size_in_memory:
                    # Se o actual size for maior ou igual ao tamanho do processo, indica
                    # que achamos um espaço onde o processo caiba, logo, colocamos ele
                    # nessa parte da memória.
                    # No caso do do atributo de end, como sabemos que o tamanho na memória
                    # é o suficiente para alocar o processo, entâo somamos o tamanho do
                    # processo ao índice de início, subtraindo 1 para ocupar os espaços
                    # necessários para a alocação do processo.
                    self._insert_process_in_memory(p, start, start + p.size_in_memory - 1)
                    return
            else:
                # Reseta o contador para 0 caso o bloco não esteja livre
                actual_size = 0

        print("Não há espaço suficiente na memória para o processo.")

    def write_using_best_fit(self, p: Process) -> None:
        actual_size = 0
        start = -1
        for i, block in enumerate(self._physical_memory + [None]):  # Truque para lidar com o último espaço
            if block is None:
                if actual_size == 0:
                    start = i
                actual_size += 1
            if block is not None or i == len(self._physical_memory):  # Final de um espaço livre ou fim da memória
                if actual_size == p.size_in_memory:  # Ajuste perfeito encontrado
                    self._insert_process_in_memory(p, start, start + actual_size - 1)
                    return  # Aloca imediatamente e retorna
                actual_size = 0
                start = -1

        print("Não há espaço suficiente na memória para o processo.")
    
    def write_using_worst_fit(self, p: Process) -> None:
        pass

    def _insert_process_in_memory(self, p: Process, start: int, end: int):
        ''' Method to insert a process in memory '''
        if end < len(self._physical_memory):
            # Entra no bloco após ter a certeza que o end seja menor que o tamanho da memória
            process_id = f"P{self._process_counter}"  # Cria o processo para Px, onde X é o atual processo
            self._process_map[p.uid] = process_id  # Mapeia o UID para o ID acima
            self._process_counter += 1
            for i in range(start, end + 1):
                self._physical_memory[i] = p.uid  # Usa o UID para rastrear qual processo ocupa o espaço
        else:
            print("Erro: Tentativa de inserir processo além do limite da memória física.")


    def memory_status(self):
        ''' Method to return a simulation of memory '''
        for i, uid in enumerate(self._physical_memory):
            if uid is None:
                print("None | ", end='')
            else:
                # Obtém o ID mapeado ou "Desconhecido"
                process_id = self._process_map.get(uid, "Desconhecido") 
                print(f"{process_id} | ", end='')
        print()  # Nova linha no final para padronizar o print do código

