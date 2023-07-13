from questoes import Questao1, Questao2


print('Olá, seja bem vindo ao próximo nível de aprendizado para melhores estudos')
start = input('podemos começar ?[S/N] ')
if start.upper() == 'S':
    print('começaremos com uma pequena revisão sobre números atômicos')
    Questao1()
    print('após vermos números atômicos, que tal vermos Símbolos ?')
    Questao2()
else:
    print('até logo!')
