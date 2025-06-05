from datetime import datetime, date, timedelta
from modules.Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, endereco, telefone, dt_nascimento, pis: str, dt_entrada: date, dt_saida: date = None): # type: ignore
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
        self.ferias = []  # ← adicionando lista de férias

    def definir_data_saida(self, data):
        hoje = date.today()

        if isinstance(data, str):
            data = datetime.strptime(data, '%d/%m/%Y').date()
        elif not isinstance(data, date):
            print("A data deve ser uma string no formato 'dd/mm/aaaa'")
            return

        limite = hoje - timedelta(days=7)
        if data < limite or data > hoje:
            print(f"A data de saída deve estar entre hoje e no máximo 7 dias atrás.")
            return

        self.dt_saida = data

    def registrar_ferias(self, inicio, fim):
        if isinstance(inicio, str):
            inicio = datetime.strptime(inicio, '%d/%m/%Y').date()
        if isinstance(fim, str):
            fim = datetime.strptime(fim, '%d/%m/%Y').date()

        if not isinstance(inicio, date) or not isinstance(fim, date):
            print("As datas devem ser string no formato 'dd/mm/yyyy' ou objeto date.")
            return

        if inicio > fim:
            print("A data de início não pode ser maior que a data de fim.")
            return

        self.ferias.append((inicio, fim))

    def Informacoes(self):
        info = super().Informacoes()
        if self.dt_saida is not None:
            info += f"""Pis: {self.pis}
        Data de Entrada: {self.dt_entrada.strftime('%d/%m/%Y')}
        Data de Saída: {self.dt_saida.strftime('%d/%m/%Y')}
"""
        else:
            info += f"""Pis: {self.pis}
        Data de Entrada: {self.dt_entrada.strftime('%d/%m/%Y')}
"""

        if self.ferias:
            info += "        Férias:\n"
            for i, (inicio, fim) in enumerate(self.ferias, 1):
                info += f"            {i}. {inicio.strftime('%d/%m/%Y')} até {fim.strftime('%d/%m/%Y')}\n"

        return info

    def __str__(self) -> str:
        data_saida_formatada = self.dt_saida.strftime('%d/%m/%Y') if self.dt_saida else "Funcionário ativo"
        ferias_txt = ""
        if self.ferias:
            ferias_txt += "Férias:\n"
            for i, (inicio, fim) in enumerate(self.ferias, 1):
                ferias_txt += f"  {i}. {inicio.strftime('%d/%m/%Y')} até {fim.strftime('%d/%m/%Y')}\n"

        return (
            f"\nNome: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"PIS/PASEP: {self.pis}\n"
            f"Endereço: {self.endereco}\n"
            f"Telefone: {self.telefone}\n"
            f"Data de Nascimento: {self.dt_nascimento.strftime('%d/%m/%Y')}\n"
            f"Data de Entrada: {self.dt_entrada.strftime('%d/%m/%Y')}\n"
            f"Data de Saída: {data_saida_formatada}\n"
            f"{ferias_txt}"
        )
