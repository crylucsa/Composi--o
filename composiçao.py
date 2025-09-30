class Processador:
    def __init__(self, modelo:str, frequencia_ghz:float,):
        self.modelo = modelo 
        self.frequencia_ghz = frequencia_ghz

    def modelo(self):
        return self.modelo
    
    def frequencia(self):
        return self.frequencia_ghz
    
    def __str__(self):
        return f"Processador: {self.modelo}, Frequencia: {self.frequencia_ghz}ghz"
    # metodo especial para representar o objeto como string
# -----------------------------------------------------------------------------------
class MemoriaRam:
    def __init__(self,capacidade_gb, tipo):
        self.capacidade_gb = capacidade_gb
        self.tipo = tipo
    
    def capacidade(self):
        return self.capacidade_gb
    
    def tipo(self):
        return self.tipo
    
    def __str__(self):
        return f"Memoria RAM: {self.capacidade_gb}GB, Tipo: {self.tipo}"
    # metodo especial para representar o objeto como string
# ----------------------------------------------------------------------------------
class Armazenamento:
    def __init__(self,capacidade_gb, tipo):
        self.capacidade_gb = capacidade_gb
        self.tipo = tipo
    
    def capacidade(self):
        return self.capacidade_gb
    
    def tipo(self):
        return self.tipo
    # metodo especial para representar o objeto como string
# ---------------------------------------------------------------------------------   
    def __str__(self):
        return f"armazenamento: {self.capacidade_gb}gb, tipo: {self.tipo}"
class Computador:
    def __init__(self, marca: str, modelo: str, proc_modelo: str, proc_vel: float,
                 ram_capacidade: int, ram_tipo: str, arm_tipo: str, arm_capacidade: int):
        self.__marca = marca
        self.__modelo = modelo
        # composiçao: os componentes so existem dentro do computador
        self.__processador = Processador(proc_modelo, proc_vel)
        self.__memoria_ram = MemoriaRam(ram_capacidade, ram_tipo)
        self.__armazenamento = Armazenamento(arm_capacidade, arm_tipo)

    def get_marca(self):
            return self.__marca

    def get_modelo(self):
            return self.__modelo

    def get_processador(self):
            return self.__processador

    def get_memoria_ram(self):
            return self.__memoria_ram

    def get_armazenamento(self):
            return self.__armazenamento
    # metodo especial para representar o objeto como string
# --------------------------------------------------------------------------------
    def ligar(self):
            print (f"ligando o computador com {self.get_marca()}    {self.get_modelo()}...")
            print (self.get_processador())
            print (self.get_memoria_ram())
            print (self.get_armazenamento())
            return self 
    #permite o encadeamento de metodos
# --------------------------------------------------------------------------------
    def __str__(self):
        return (f"Computador: {self.__marca} {self.__modelo}\n"
                f"  {self.__processador}\n"
                f"  {self.__memoria_ram}\n"
                f"  {self.__armazenamento}")

    def __del__(self):
        print(f"O computador {self.__marca} {self.__modelo} foi destruído.")
        print("seus componentes tambem deixam de existir")

# metodo especial chamado quando o objeto eh destruido
# -------------------------Teste-------------------------------------------------------

meu_pc = Computador("Dell", "Inspiron 15", 
                    "Intel i7-12700H", 2.7, 
                    16, "DDR4", 
                    "SSD", 240)

print(meu_pc)   # representação amigável
meu_pc.ligar()  # liga e mostra os componentes
# del meu_pc    # destrói o objeto e seus componentes