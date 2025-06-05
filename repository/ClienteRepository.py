from modules.Cliente import Cliente
from datetime import datetime

clientes = []

def adicionar(pessoa: Cliente):
    if not all([pessoa.nome, pessoa.endereco, pessoa.cpf, pessoa.dt_cadastro]):
        raise ValueError("Todos os campos devem ser preenchidos.")
    
    if pessoa in clientes:
        print(f"O cliente {pessoa.nome} já está cadastrado.")
        return

    clientes.append(pessoa)
    print(f"Cliente {pessoa.nome} adicionado com sucesso.")

def localizar_cliente_por_cpf(cpf: str):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None



def exibir_Lista_Clientes():
    if not clientes:
        return "Nenhum cliente cadastrado."
    resultado = "\n****    Lista de Clientes    ****\n"
    for cliente in clientes:
        resultado += f"\nCliente:\n{cliente}\n"
    return resultado

def excluir_cliente_por_cpf(cpf: str):
    cliente = localizar_cliente_por_cpf(cpf)
    if cliente:
        clientes.remove(cliente)
        print(f"Cliente {cliente.nome} com CPF {cpf} foi removido com sucesso.")
    else:
        print(f"Nenhum cliente com CPF {cpf} foi encontrado.")


def editar_Dados_Cliente_por_cpf(cpf:str):
    cliente = localizar_cliente_por_cpf(cpf)
    if not cliente:
        print(f"Nenhum cliente cadastradp com o cpf {cpf}.")
        return
    print(f"Quais dados deseja altterar")