from modules.Funcionario import Funcionario
'''
  - CRUD Funcionario
'''
funcs = []

def adicionar_Funcio(funcionario:Funcionario):
    if not all([funcionario.nome, funcionario.cpf, funcionario.endereco, funcionario.dt_nascimento, funcionario.pis, funcionario.dt_entrada]):
        return f"É necessario preencher todos os dados para cadastraro funcionario."
    funcs.append(funcionario)
    return f"O funcionario {funcionario.nome}, foi adicionado com sucesso."

def exibir_lista_funcionarios():
    if not funcs:
        return "A lista esta vazia"
    saida = "****    LISTA DE FUNCIONARIOS    ****\n\n"
    for funcionario in funcs:
        saida += f"{funcionario}\n\n"
    return saida


def localizar_funcionario_por_cpf(cpf):
    if not funcs:
        return "A lista está vazia."
    for func in funcs:
        if func.cpf == cpf:
            return func
    return f"Nenhum funcionario localizado com o CPF: {cpf}"

def localiza_funcionario_por_pis(pis):
    if not funcs:
        return "A lista está vazia."
    for func in funcs:
        if func.pis == pis:
            return f"funcionario localizado \n{func}"
    return f"Nenhum funcionario localizado com o PIS/PASEP: {pis}"

def adicionar_saida_funcionario_por_cpf(cpf, data):
    func = localizar_funcionario_por_cpf(cpf)
    if isinstance(func, Funcionario):
        func.definir_data_saida(data)
        return f"Data de saida registrada para {func.nome}"
    else:
        return func
    

def excluir_funcionario_por_cpf(cpf):
    for i, func in enumerate(funcs):
        if func.cpf == cpf:
            funcs.pop(i)
            return f"Funcionário com nome {func.nome} e CPF {cpf} removido com sucesso."
    return f"Nenhum funcionário localizado com o CPF {cpf}."


def registrar_ferias_funcionario_por_cpf(cpf, inicio, fim):
    func = localizar_funcionario_por_cpf(cpf)
    if isinstance(func, Funcionario):
        func.registrar_ferias(inicio, fim)
        return f"Férias registradas para o funcionário {func.nome}."
    return func  
