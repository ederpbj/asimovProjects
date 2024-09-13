def soma_um(numero):
    return numero +1

def function_call(function):
    numero_to_add = 5
    return function(numero_to_add)

print(function_call(soma_um))

def funcao_ola():
    def diga_oi():
        return "Hi"
    return diga_oi

hello = funcao_ola()
print(hello())

def decorador_maiusculo(function):
    def wrapper():
        func = function()
        cria_maisculo = func.upper()
        return cria_maisculo
    return wrapper()

def diga_oi():
    return 'hello there'

funcao_decoradora = decorador_maiusculo(diga_oi)

print(funcao_decoradora)

# tem o mesmo efeito da anterior
@decorador_maiusculo
def diga_ola():
    return 'hi friends'

print(diga_ola)

