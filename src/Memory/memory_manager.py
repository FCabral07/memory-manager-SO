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
        print("Inicializando o MemoryManager com a estratégia:", strategy.name)
        self._strategy = strategy
        self._physical_memory: List[str] = [None] * 128
        # Mapeando o processo para printar ao invés do código
        self._process_map = {}
        self._process_counter = 1

    def write(self, p: Process) -> None:
        ''' Selector method for choice what kind of algorithm to use '''
        print(f"Tentando escrever o processo {p.uid} usando a estratégia {self._strategy.name}")
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
        print(f"Deletando o processo {p.uid} da memória")
        for i, uuid in enumerate(self._physical_memory):
            if uuid == p.uid:
                self._physical_memory[i] = None
                
        self._process_map.pop(p.uid, None)

    def write_using_first_fit(self, p: Process) -> None:
        ''' Method for write a process using first fit '''
        print(f"Escrevendo o processo {p.uid} usando First Fit")
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
        ''' Method for write a process using best fit '''
        print(f"Escrevendo o processo {p.uid} usando Best Fit")
        best_fit_start = None # Define o início do best fit
        best_fit_size = float('inf') # Define como tamanho infinito, com isso, posso ir diminuindo o tamanho até o best fit
        actual_size = 0
        start = None

        # Adiciono o None abaixo ao final para o algoritmo na hora de percorrer a memória possa considerar também o último
        # espaço. Sem o None ele não vai considerar o último espaço.
        extended_memory = self._physical_memory + [None]

        # Percorrendo a memória
        for i, block in enumerate(extended_memory):
            # Se o bloco for None
            if block is None:
                # Se o começo do bloco livre for None
                if start is None:
                    # O começo se torna a posição i
                    start = i
                # Aumento em 1 o tamanho do espaço livre atual enquanto for None
                actual_size += 1
            # Se o bloco não for None ou chegar ao fim da memória
            if block is not None or i == len(extended_memory) - 1:
                # Se o start não for None E o tamanho atual livre da memória for maior que o tamanho do processo
                if start is not None and actual_size >= p.size_in_memory:
                    # Se o best fit size for None OU o tamanho atual livre da memória for maior que 0 e menor que o best fit size
                    if best_fit_size is None or (0 < actual_size < best_fit_size):
                        # Novo best fit encotnrado, atribuo seu endereço
                        best_fit_size = actual_size
                        best_fit_start = start
                # Reseta para o próximo segmento
                actual_size = 0
                start = None

        # Se o best fit start não for None
        if best_fit_start is not None:
            # Aloca o processo na posição do melhor ajuste
            self._insert_process_in_memory(p, best_fit_start, best_fit_start + p.size_in_memory - 1)
        else:
            # Se nenhum espaço adequado foi encontrado
            print("Não há espaço suficiente na memória para o processo.")

    def write_using_worst_fit(self, p: Process) -> None:
        print(f"Escrevendo o processo {p.uid} usando Worst Fit")

    def _insert_process_in_memory(self, p: Process, start: int, end: int):
        ''' Method to insert a process in memory '''
        print(f"Inserindo o processo {p.uid} na memória, do bloco {start} até {end}")
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
        print("Status atual da memória:")
        for i, uid in enumerate(self._physical_memory):
            if uid is None:
                print("None | ", end='')
            else:
                # Obtém o ID mapeado ou "Desconhecido"
                process_id = self._process_map.get(uid, "Desconhecido") 
                print(f"{process_id} | ", end='')
        print()  # Nova linha no final para padronizar o print do código
