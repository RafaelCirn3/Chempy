from mendeleev import element as elemento

from translate import Translator

translator = Translator(to_lang="pt")


def descricaoElemento(elem):
    element = elemento([elem])
    return translator.translate(element.name)


userElem = input("Digite um elemento ao qual você deseja saber mais sobre: ")
print(descricaoElemento(userElem))
