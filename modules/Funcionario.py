from datetime import datetime, date
from modules.Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, endereco, telefone, dt_nascimento, pis: str, dt_entrada: date, dt_saida: date = None):

        if isinstance(dt_nascimento, str):
            dt_nascimento = datetime.strptime(dt_nascimento, '%d/%m/%Y').date()
        elif not isinstance(dt_nascimento, date):
            raise ValueError("dt_nascimento deve ser uma string no formato 'dd/mm/yyyy' ou um objeto date.")

        if isinstance(dt_entrada, str):
            dt_entrada = datetime.strptime(dt_entrada, '%d/%m/%Y').date()
        elif not isinstance(dt_entrada, date):
            raise ValueError("dt_entrada deve ser uma string no formato 'dd/mm/yyyy' ou um objeto date.")

        if dt_saida is not None:
            if isinstance(dt_saida, str):
                dt_saida = datetime.strptime(dt_saida, '%d/%m/%Y').date()
            elif not isinstance(dt_saida, date):
                raise ValueError("dt_saida deve ser uma string no formato 'dd/mm/yyyy', um objeto date ou None.")

        super().__init__(nome, cpf, endereco, telefone, dt_nascimento)
        self.pis = pis
        self.dt_entrada = dt_entrada
        self.dt_saida = dt_saida

        
    def Informacoes(self):
        info =super().Informacoes()        
        if self.dt_saida is not None:
            return info+ f"""Pis: {self.pis}
            data de Entrada: {self.dt_entrada}
            Data Saida: {self.dt_saida}
            """
        else:
            return info +f"""Pis: {self.pis}
        data de Entrada: {self.dt_entrada}
        """

            
            
            
            
    def definir_data_saida(self, data:date.today):
        self.dt_saida = data