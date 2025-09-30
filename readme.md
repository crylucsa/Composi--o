🖥️ Exercício: Criação e Composição de Objetos (Computador e Componentes)

Este projeto demonstra o conceito de composição em Programação Orientada a Objetos (POO), utilizando Python.
A ideia é modelar um computador e seus componentes essenciais (processador, memória RAM e armazenamento) de forma que os componentes façam parte do computador e não existam de forma independente.

📌 Estrutura do Código
Classes Implementadas

Processador

Atributos:

modelo (str)

frequencia_ghz (float)

Métodos:

modelo() → retorna o modelo.

frequencia() → retorna a frequência.

__str__() → retorna uma representação amigável.

MemoriaRam

Atributos:

capacidade_gb (int)

tipo (str)

Métodos:

capacidade() → retorna a capacidade.

tipo() → retorna o tipo (DDR4, DDR5 etc).

__str__() → retorna uma representação amigável.

Armazenamento

Atributos:

capacidade_gb (int)

tipo (str) → SSD ou HDD.

Métodos:

capacidade() → retorna a capacidade.

tipo() → retorna o tipo.

__str__() → retorna uma representação amigável.

Computador

Atributos:

marca (str)

modelo (str)

Composição:

Processador

MemoriaRam

Armazenamento

Métodos:

get_marca(), get_modelo(), get_processador(), get_memoria_ram(), get_armazenamento() → acessam atributos e componentes.

ligar() → simula ligar o computador e imprime suas especificações. Retorna self para permitir encadeamento de métodos.

__str__() → representação amigável do computador.

__del__() → mostra mensagem de destruição do objeto, reforçando que seus componentes deixam de existir junto com ele.

🚀 Conceito de Composição

A composição garante que os componentes (Processador, MemoriaRam e Armazenamento) não existam de forma independente.

Eles são criados dentro do construtor do Computador e deixam de existir quando o computador é destruído.

Exemplo no código:

self.__processador = Processador(proc_modelo, proc_vel)
self.__memoria_ram = MemoriaRam(ram_capacidade, ram_tipo)
self.__armazenamento = Armazenamento(arm_capacidade, arm_tipo)

📂 Cenário de Teste
meu_pc = Computador("Dell", "Inspiron 15", 
                    "Intel i7-12700H", 2.7, 
                    16, "DDR4", 
                    "SSD", 240)

print(meu_pc)   # representação amigável
meu_pc.ligar()  # liga e mostra os componentes

Saída esperada:
Computador: Dell Inspiron 15
  Processador: Intel i7-12700H, Frequencia: 2.7GHz
  Memória RAM: 16GB, Tipo: DDR4
  Armazenamento: 240GB, Tipo: SSD

ligando o computador com Dell Inspiron 15...
Processador: Intel i7-12700H, Frequencia: 2.7GHz
Memória RAM: 16GB, Tipo: DDR4
Armazenamento: 240GB, Tipo: SSD

🗑️ Destruição do Objeto

Se o computador for destruído manualmente com:

del meu_pc


A saída será:

O computador Dell Inspiron 15 foi destruído.
seus componentes tambem deixam de existir

📖 Conclusão

Este exemplo mostra como:

Criar classes representando partes de um sistema.

Usar composição para modelar relações de dependência forte.

Implementar métodos especiais (__str__, __del__) para melhorar legibilidade e reforçar conceitos de ciclo de vida do objeto.