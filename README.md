# Simulação de Sistema Operacional

Este projeto é uma simulação do funcionamento de um Sistema Operacional (SO), desenvolvido como parte de um projeto universitário. O foco está em ilustrar como diferentes algoritmos de gerenciamento de memória operam dentro de um SO, incluindo Best Fit, First Fit e Worst Fit. A simulação visa proporcionar uma compreensão prática dos conceitos fundamentais do SO e sua gestão de recursos.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- **Raiz do Projeto**:
  - `requirements.txt`: Contém todas as bibliotecas Python usadas no projeto. Para instalar, use `pip install -r requirements.txt`.
  - `.vscode/`: Pasta com configurações do VSCode utilizadas durante o desenvolvimento.
  - `src/`: Pasta contendo o código-fonte do projeto.

- **Pasta src**:
  - **CPU/**: Simula o funcionamento da CPU. Contém:
    - `cpu_manager.py`: Gerencia as operações da CPU (atualmente não utilizado).
  - **Memory/**: Representa a memória e suas estratégias de gerenciamento. Contém:
    - `strategy.py`: Enumerações das estratégias de gerenciamento de memória.
    - `memory_manager.py`: Gerenciador de memória, onde ocorrem as operações como adição e remoção de processos.
    - `address_memory.py`: Utilizado para representar endereços na memória (pouco usado).
  - **Schedule/**: (Atualmente não utilizado).
  - **SO/**: Contém as operações e simulações do Sistema Operacional. Inclui:
    - `main.py`: Arquivo principal para executar o projeto.
    - `process.py`: Simula um processo no SO.
    - `system_call_type.py`: Tipos de operações de sistema, usando enum.
    - `system_operation.py`: Operações do sistema, como criar, escrever e deletar um processo.

## Como Executar

Para executar a simulação, siga os passos abaixo:

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até a pasta do projeto e instale as dependências usando: `pip install -r requirements.txt`
3. Para iniciar a simulação, navegue até a pasta `src/SO` e execute o arquivo `main.py` com o comando: `python main.py`

## Para alterar os algoritmos
- Vá na pasta `src/SO/system_operation.py`, vá na função system_call e mude a linha 50 para o método desejado: *BEST_FIT*, *WORST_FIT* ou *FIRST_FIT*
