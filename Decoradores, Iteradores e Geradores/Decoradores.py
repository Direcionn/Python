#Decorador simples - Usado o '@' para simplificar o código
def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar.')
        funcao()
        print('Faz algo depois de executar.')
    
    return envelope

@meu_decorador
def ola_mundo():
    print('Olá mundo.')

ola_mundo()


#Decorador com argumentos - Pode-se usar '*args' e '**kwargs' para se passar os argumentos
def Duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    
    return envelope

@Duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo {tecnologia}.')

aprender('Python')

#Introspecção - É a capacidade de um objeto saber seus proprios atributos em tempo de execução
import functools

def Duplicar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    
    return envelope

@Duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo {tecnologia}.')

aprender('Python')
print(aprender.__name__)    #Retorna 'aprender'



