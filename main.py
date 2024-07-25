class Main:
    pass

from cliente import Cliente

from conta import Conta 

c1= Cliente("Jonas", "121545115")
conta = Conta(c1.get_nome(), 1222, 0)

conta.deposita(1000)
conta.sacar(50)
conta.extrato()

print(conta.titular, "Numero", conta.numero, "Seu Saldo", conta.saldo)