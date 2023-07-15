
from mendeleev import element  # biblioteca com elementos e propriedades da tabela de mendeleev
from translate import Translator

translator = Translator(to_lang="pt")


def informacoeselem():
    element_symbol = input("Digite o símbolo do elemento: ")
    info_choice = int(input("Digite:\n1 - para obter o nome do elemento\n2 - para obter o número atômico\n3 - para obter a massa molar g/mol\n4 - para obter todas as informações\nEscolha: "))
    
    try:
        chem_element = element(element_symbol)
        atomic_number = chem_element.atomic_number
        element_name = chem_element.name
        atomic_weight = chem_element.atomic_weight
        
        if info_choice == 1:
            info = element_name
            question = f"Qual é o nome do elemento com o símbolo {element_symbol}?"
        elif info_choice == 2:
            info = atomic_number
            question = f"Qual é o número atômico do elemento com o símbolo {element_symbol}?"
        elif info_choice == 3:
            info = atomic_weight
            question = f"Qual é a massa molar g/mol com o símbolo {element_symbol}?"
        elif info_choice == 4:
            info = f"Nome: {translator.translate(element_name)}\nNúmero atômico: {atomic_number}\nMassa molar: {atomic_weight}g/mol"
            question = f"Informações completas do elemento com o símbolo {element_symbol}:"
        else:
            print("Escolha inválida. Tente novamente.")
            return None, None
        
        return question, info
    
    except ValueError:
        print("Elemento inválido. Verifique o símbolo e tente novamente.")


pergunta, res = informacoeselem()
print(pergunta)
print(res)


def Correcao(questao, resposta):
    user_resposta = input(questao + " ")
    
    if user_resposta == str(resposta):
        print("Resposta correta! Parabéns!")
    else:
        print("Resposta incorreta.")
        print("A resposta correta é:", resposta)

def QuestMaker():
    formula = input("Digite a fórmula química: ")
    
    # Extrai os elementos e suas quantidades da fórmula
    elements = {}
    current_element = ""
    current_count = ""
    for char in formula:
        if char.isnumeric():
            current_count += char
        else:
            if current_element:
                count = int(current_count) if current_count else 1
                if current_element in elements:
                    elements[current_element] += count
                else:
                    elements[current_element] = count
            current_element = char
            current_count = ""
    
    # Adiciona o último elemento à lista
    if current_element:
        count = int(current_count) if current_count else 1
        if current_element in elements:
            elements[current_element] += count
        else:
            elements[current_element] = count
    # Calcula a massa molar total com base nos elementos e suas quantidades
    massamolar = 0
    for element_symbol, count in elements.items():
        elemento_quimico = element(element_symbol)
        peso_atomico = elemento_quimico.atomic_weight
        massamolar += peso_atomico * count
    
    questao = f"Qual é a massa molar de {formula}?"
    return questao, massamolar

# Exemplo de uso
quest, ans = QuestMaker()
Correcao(quest, ans)


