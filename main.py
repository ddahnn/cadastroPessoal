from modules.Cliente import Cliente
from modules.Funcionario import Funcionario
from repository.ClienteRepository import adicionar, localizar_cliente_por_cpf, exibir_Lista_Clientes, excluir_cliente_por_cpf
from repository.FuncionarioRepository import adicionar_Funcio, exibir_lista_funcionarios, localizar_funcionario_por_cpf, localiza_funcionario_por_pis, adicionar_saida_funcionario_por_cpf,excluir_funcionario_por_cpf, registrar_ferias_funcionario_por_cpf

# Criando cliente
c1 = Cliente("João", "123.456.789-00", "Rua algum lugar ai 66", "51 99999-9999", "01/01/1990", "04/06/2025") 
c2 = Cliente("Maria", "111.1111.111-11", "Rua das Flores 123", "21 98888-8888", "15/05/1985", "10/10/2024") 
c3 = Cliente("João", "222.2222.222-22", "Avenida Central 456", "31 97777-7777", "30/08/1990", "12/12/2023") 
c4 = Cliente("Ana", "333.3333.333-33", "Travessa da Paz 789", "41 96666-6666", "02/02/1978", "01/01/2026") 
c5 = Cliente("Carlos", "444.4444.444-44", "Praça do Sol 101", "51 95555-5555", "09/09/2000", "05/05/2027") 
c6 = Cliente("Fernanda", "555.5555.555-55", "Rua Nova 202", "61 94444-4444", "12/12/1995", "08/08/2028") 
c7 = Cliente("Lucas", "666.6666.666-66", "Alameda Verde 303", "71 93333-3333", "25/03/1988", "03/03/2029") 
c8 = Cliente("Patricia", "777.7777.777-77", "Estrada Velha 404", "81 92222-2222", "18/07/1975", "07/07/2030") 
print(exibir_Lista_Clientes())


# Adicionando cliente ao "banco"
adicionar(c1)
adicionar(c2)
adicionar(c5)
adicionar(c6)
adicionar(c7)


print(" Realizando compras ")
print(c1.adicionar_valor_compras(5000))   
print(c1.adicionar_valor_compras(900.00)) 
print(c1.adicionar_valor_compras(10.0)) 
print(c1.adicionar_valor_compras(100))   
print(c1.adicionar_valor_compras(-20)) 

print("Mostrando informações")
print(c1.Informacoes())   
#print(c1._qualidade_cliente())           

print("Buscando pelo CPF")
print(localizar_cliente_por_cpf("000.0000.000-00"))

print("Exibindo lista")
print(exibir_Lista_Clientes())

excluir_cliente_por_cpf("666.6666.666-66")

print("Exibindo lista")
print(exibir_Lista_Clientes())





print(f"Área funcionario")

f1 = Funcionario("adalberto", "654.987.321-11", "lugar nenhum 666", "51 99999-9999", "21/01/1993", "000.0000.000-00", "05/06/2025") # type: ignore
f2 = Funcionario("Beatriz", "123.123.123-12", "Rua das Palmeiras 10", "51 98888-8888", "10/02/1988", "111.1111.111-11", "12/12/2026" )# type: ignore
f3 = Funcionario("Carlos", "321.321.321-21", "Avenida Brasil 200", "51 97777-7777", "05/05/1990", "222.2222.222-22", "01/01/2027") # type: ignore
f4 = Funcionario("Daniela", "456.456.456-45", "Travessa Azul 55", "51 96666-6666", "15/09/1985", "333.3333.333-33", "30/06/2028") # type: ignore
f5 = Funcionario("Eduardo", "789.789.789-78", "Praça Central 99", "51 95555-5555", "22/11/1992", "444.4444.444-44", "20/08/2029") # type: ignore

print(f1.Informacoes())


f1.definir_data_saida("02/06/2025")

print(f1.Informacoes())

print("****    Aficionando funcionarios a lista    ****")
print(adicionar_Funcio(f1))
print(adicionar_Funcio(f2))
print(adicionar_Funcio(f3))
print(adicionar_Funcio(f4))
print(adicionar_Funcio(f5))


print("\n\n****    Exibindo lista de Funcionarios    ****\n\n")

print(exibir_lista_funcionarios())

print(f"****    Localizando Funcionario.    ****\n\n")
print(localizar_funcionario_por_cpf("654.987.321-11"))
print(localizar_funcionario_por_cpf("789.789.789-78"))

print(localiza_funcionario_por_pis("222.2222.222-22"))
print(localiza_funcionario_por_pis("999.999.999-99"))

print('\n\n****    SAIDA DE FUNCIONARIO    ****\n\n')
print(adicionar_saida_funcionario_por_cpf('654.987.321-11', "04/06/2025"))


print(localizar_funcionario_por_cpf("654.987.321-11"))



print("\n\n****    Exibindo lista de Funcionarios    ****\n\n")

print(exibir_lista_funcionarios())


print(excluir_funcionario_por_cpf('654.987.321-11'))

print(exibir_lista_funcionarios())

print(registrar_ferias_funcionario_por_cpf('789.789.789-78', "05/06/2025","04/05/2025"))