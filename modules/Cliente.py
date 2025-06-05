from modules.Pessoa import Pessoa
from datetime import date, datetime

class Cliente(Pessoa):
    def __init__(self, nome, cpf, endereco, telefone, dt_nascimento, dt_cadastro, valor_gasto: float = 0.0):
        # Tratamento de dt_nascimento
        if isinstance(dt_nascimento, str):
            dt_nascimento = datetime.strptime(dt_nascimento, '%d/%m/%Y').date()
        elif not isinstance(dt_nascimento, date):
            raise ValueError("dt_nascimento deve ser uma string no formato 'dd/mm/yyyy' ou um objeto date.")
        
        # Tratamento de dt_cadastro
        if isinstance(dt_cadastro, str):
            dt_cadastro = datetime.strptime(dt_cadastro, '%d/%m/%Y').date()
        elif not isinstance(dt_cadastro, date):
            raise ValueError("dt_cadastro deve ser uma string no formato 'dd/mm/yyyy' ou um objeto date.")

        super().__init__(nome, cpf, endereco, telefone, dt_nascimento)
        self.dt_cadastro = dt_cadastro
        self.valor_gasto = valor_gasto
        self.qualidade_cli = self.__definir_nivel_cliente()

    def _qualidade_cliente(self):
        if self.qualidade_cli == 0:
            return f"O cliente {self.nome}, não possui compras."
        return f"O cliente {self.nome} está no nível {self.qualidade_cli}"

    def adicionar_valor_compras(self, valor: float):
        if valor < 0:
            return "Impossível adicionar um valor negativo."
        self.valor_gasto += valor
        self.qualidade_cli = self.__definir_nivel_cliente()
        print(f"Valor adicionado ao histórico do cliente {self.nome}.")
        return f"Valor total gasto: R$ {self.valor_gasto:.2f}"

    def __definir_nivel_cliente(self):
        if self.valor_gasto < 1000.00:
            return 0
        elif self.valor_gasto < 2000.00:
            return 1
        elif self.valor_gasto < 3000.00:
            return 2
        elif self.valor_gasto < 4000.00:
            return 3
        elif self.valor_gasto < 5000.00:
            return 4
        elif self.valor_gasto < 6000.00:
            return 5
        elif self.valor_gasto < 7000.00:
            return 6
        elif self.valor_gasto < 8000.00:
            return 7
        elif self.valor_gasto < 9000.00:
            return 8
        elif self.valor_gasto < 10000.00:
            return 9
        else:
            return 10

    def Informacoes(self):
        info = super().Informacoes()
        return info + f"""Data de cadastro: {self.dt_cadastro}
        Qualidade do cliente:  {self.qualidade_cli}
        valor gasto: {self.valor_gasto}
        """

    def __str__(self) -> str:
        return (
            f"Nome: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"Endereço: {self.endereco}\n"
            f"Telefone: {self.telefone}\n"
            f"Data de Nascimento: {self.dt_nascimento.strftime('%d/%m/%Y')}\n"
            f"Data de Cadastro: {self.dt_cadastro.strftime('%d/%m/%Y')}\n"
            f"Valor Gasto: R$ {self.valor_gasto:.2f}\n"
            f"Qualidade do Cliente: {self.qualidade_cli}\n"
        )
