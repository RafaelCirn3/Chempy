
from mendeleev import element as elemento  # biblioteca com elementos e propriedades da tabela de mendeleev
from molmass import ELEMENTS
from translate import Translator

translator = Translator(to_lang="pt")

def Questao1():
    print('-=-'*32)
    c, h, o, p, k = elemento(['C', 'H', 'O', 'P', 'K'])
    print(c.atomic_number, h.atomic_number, o.atomic_number, p.atomic_number, k.atomic_number)
    resposta = input('Sabendo que cada número representa o número atômico de um Elemento, qual desses representa o Fósforo ? ')
    while True:
        if resposta == '15':
            print('Resposta correta!')
            break
        else:
            resposta = input('Resposta incorreta. Tente novamente: ')
    print('-=-'*32)


def Questao2():

    h, he, hs = elemento(['H', 'He', 'Hs'])
    print(h.symbol, ', ', he.symbol, ', ', hs.symbol)
    resposta = input('qual desses representa o elemento Hélio ? ')
    while True:
        if resposta.lower() == 'he':
            print('Resposta correta!')
            break
        else:
            resposta = input('Resposta incorreta. Tente novamente: ')
    print('-=-'*32)


def Questao3():


