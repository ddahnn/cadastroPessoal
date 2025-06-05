from modules.Cliente import Cliente
from modules.Funcionario import Funcionario
from repository.ClienteRepository import adicionar, localizar_cliente_por_cpf, exibir_Lista_Clientes, excluir_cliente_por_cpf

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

f1 = Funcionario("adalberto","654.987.321-11", "lugar nenhum 666", "51 99999-9999", "21/01/1993", "000.0000.000-00", "05/06/2025", None)

print(f1.Informacoes())