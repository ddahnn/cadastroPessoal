from datetime import date, datetime
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str, endereco: str, telefone: str, dt_nascimento: date):
        self.nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._telefone = telefone
        self._dt_nascimento = dt_nascimento

        if isinstance(dt_nascimento, str):
            self._dt_nascimento = datetime.strptime(dt_nascimento, '%d/%m/%Y').date()
        elif isinstance(dt_nascimento, date):
            self._dt_nascimento = dt_nascimento
        else:
            raise TypeError("dt_nascimento deve ser uma string no formato 'dd/mm/yyyy' ou um objeto date")

    @property
    def cpf(self):
        return self._cpf

    @property
    def endereco(self):
        return self._endereco

    @property
    def telefone(self):
        return self._telefone

    @property
    def dt_nascimento(self):
        return self._dt_nascimento

    @abstractmethod
    def Informacoes(self):
        return f"""
****    Informações do Usuario {self.nome}    ****
        Nome: {self.nome},
        CPF: {self._cpf}
        Endereço: {self._endereco}
        Telefone: {self._telefone}
        Data de Nascimento: {self._dt_nascimento}
        """
