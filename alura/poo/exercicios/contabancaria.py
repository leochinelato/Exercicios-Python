class ContaBancaria:
    def __init__(self, titular="", saldo=float):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f"Olá {self.titular}, você possui R$ {self.saldo} na conta."

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True


titular_1 = ContaBancaria("Leonardo", 3000)
titular_2 = ContaBancaria("Cleber", 200)

print(titular_1)
print(titular_2)

titular_3 = ContaBancaria("Joao", 900)
print(f"Antes: Conta ativa? {titular_3._ativo}")
ContaBancaria.ativar_conta(titular_3)
print(f"Depois: Conta ativa? {titular_3._ativo}")
