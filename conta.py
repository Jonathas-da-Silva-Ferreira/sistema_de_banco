class Conta:
    def __init__(self, titular, numero, saldo):
        self._saldo = saldo
        self.numero = numero
        self.titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("O saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print('Saque realizado com sucesso')
        else:
            print('Saldo insuficiente')

    def deposita(self, valor):
        self._saldo += valor

    def extrato(self):
        print("Cliente: ", self.titular, "Saldo Atual: ", self._saldo)
