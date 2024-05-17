#Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo.
#Inicie o atributo ativo como False por padrão.

class ContaBancaria:
    Contas = []
    def __init__(self,titular,saldo,ativo = False):
        self.titular = titular
        self.saldo = saldo   
        self._ativo = False     
 
#Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. 
#Crie duas instâncias da classe e imprima essas instâncias.

    def __str__(self):
        return f'A conta de {self.titular} com o saldo de {self.saldo}'
    
Conta1 = ContaBancaria ('Aline', 4000)
Conta2 = ContaBancaria ('Anderson', 7000)
print(Conta1)
print(Conta2)

#Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo 
#como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

@classmethod
def ativar_conta(cls, conta):
        conta._ativo = True

Conta3 = ContaBancaria("Fernando", 1000)
print(f"Conta ativa? {Conta3._ativo}")

#Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. 
# Utilize propriedades, se necessário.

class ContaBancaria_Pythonica:
    def __init__(self, titular, saldo,ativo = False):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

# Crie uma instância da classe e imprima o valor da propriedade titular.
Conta4 = ContaBancaria_Pythonica("Afonso", 20)
print(f"Titular da conta 4: {Conta4.titular}")



