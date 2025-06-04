from modules.Pessoa import Pessoa
from datetime import date, datetime

class Cliente (Pessoa):
    def __init__(self, nome, cpf, endereco, dt_nascimento, dt_cadastro:date, valor_gasto : float= 0.0):
        super().__init__(nome, cpf, endereco, dt_nascimento)
        self.dt_cadastro = dt_cadastro
        self.valor_gasto = valor_gasto
        self.qualidade_cli = self.__definir_nivel_cliente()
        
        
        if isinstance(dt_nascimento, str):
            self.dt_nascimento = datetime.strptime(dt_nascimento, '%d/%m/%Y').date()
        elif isinstance(dt_nascimento, date):
            self.dt_nascimento = dt_nascimento
            
    def _qualidade_cliente(self):
        if self.qualidade_cli == 0:
            return f"O cliente {self.nome}, não possui compras."
        elif self.qualidade_cli ==1 :
            return  f"cliente o {self.nome} esta no nivel 1"
        elif self.qualidade_cli == 2:
            return f"cliente o {self.nome} esta no nivel 2"
        elif self.qualidade_cli == 3:
            return f"cliente o {self.nome} esta no nivel 3"
        elif self.qualidade_cli == 4:
            return f"cliente o {self.nome} esta no nivel 4"
        elif self.qualidade_cli == 5:
            return f"cliente o {self.nome} esta no nivel 5"
        elif self.qualidade_cli == 6:
            return f"cliente o {self.nome} esta no nivel 6"
        elif self.qualidade_cli == 7:
            return f"cliente o {self.nome} esta no nivel 7"
        elif self.qualidade_cli == 8:
            return f"cliente o {self.nome} esta no nivel 8"
        elif self.qualidade_cli == 9:
            return f"cliente o {self.nome} esta no nivel 9"
        elif self.qualidade_cli == 10:
            return f"cliente o {self.nome} esta no nivel 10"
        
    def adicionar_valor_compras(self, valor: float):
        if valor < 0:
            return "Impossível adicionar um valor negativo."
        self.valor_gasto += valor
        self.qualidade_cli = self.__definir_nivel_cliente()
        print(f"Valor adicionado ao histórico do cliente {self.nome}.")
        return f"Valor total gasto: R$ {self.valor_gasto:.2f}"
        
    def __definir_nivel_cliente(self):
        if self.valor_gasto == 0 and self.valor_gasto <1000.00:
            return 0
        elif self.valor_gasto > 1000.00 and self.valor_gasto < 2000.00:
            return 1
        elif self.valor_gasto >= 2000.00 and self.valor_gasto < 3000.00:
            return 2
        elif self.valor_gasto >= 3000.00 and self.valor_gasto < 4000.00:
            return 3
        elif self.valor_gasto >= 4000.00 and self.valor_gasto < 5000.00:
            return 4
        elif self.valor_gasto >= 5000.00 and self.valor_gasto < 6000.00:
            return 5
        elif self.valor_gasto >= 6000.00 and self.valor_gasto < 7000.00:
            return 6
        elif self.valor_gasto >= 7000.00 and self.valor_gasto < 8000.00:
            return 7
        elif self.valor_gasto >= 8000.00 and self.valor_gasto < 9000.00:
            return 8
        elif self.valor_gasto >= 9000.00 and self.valor_gasto < 10000.00:
            return 9
        else:
            return 10
        
        
    def Informacoes(self):
        info= super().Informacoes()
        return  info + f"""Data de cadastro: {self.dt_cadastro}
        Qualidade do cliente:  {self.qualidade_cli}
        valor gasto:{self.valor_gasto}
        """