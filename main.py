from modules.Cliente import Cliente

c1= Cliente("Daniel", "000.0000.000-00", "Algum lugar por ai 666", "21/01/1993", "04/06/2025")
c2 = Cliente("Maria", "111.1111.111-11", "Rua das Flores 123", "15/05/1985", "10/12/2024")
c3 = Cliente("João", "222.2222.222-22", "Avenida Central 456", "30/09/1978", "22/08/2026")
c4 = Cliente("Ana", "333.3333.333-33", "Praça da Paz 789", "07/03/1990", "18/11/2025")

c1.adicionar_valor_compras(5000)
c1.adicionar_valor_compras(100)
c1.adicionar_valor_compras(900.00)
c1.adicionar_valor_compras(10.0)


print(c1.Informacoes())