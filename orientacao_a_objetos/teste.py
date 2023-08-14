def cria_conta(numero,titular,saldo,limite):
    conta = {"numero":numero, "titular":titular,"saldo":saldo,"limite":limite}
    return conta

def deposita(conta,valor):
    conta["saldo"] += valor

def saque(conta,valor):
    conta["saldo"] -= valor

def extrato(conta):
    print('O seu saldo é {}'.format(conta['saldo']))

# conta = cria_conta(123,'will',100.0,1000.0)
# conta2 = cria_conta(321,'willian',50.0,100.0)

# print('Titular',conta['titular'])
# print('Titular',conta2['titular'])