from mendeleev import element


def informacoeselem(element_symbol, info_choice):
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
            info = f"Nome: {element_name}\nNúmero atômico: {atomic_number}\nMassa molar: {atomic_weight}g/mol"
            question = f"Informações completas do elemento com o símbolo {element_symbol}:"
        else:
            return "Escolha inválida. Tente novamente.", None
        
        return question, info
    
    except ValueError:
        print("Elemento inválido. Verifique o símbolo e tente novamente.")


pergunta, res = informacoeselem('Cu', 4)
print(pergunta)
print(res)

def Correcao(questao, resposta, user_resposta):
    if user_resposta == str(resposta):
        return "Resposta correta! Parabéns!"
    else:
        return f"Resposta incorreta. A resposta correta é: {resposta}"

def QuestMaker(formula):
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
    
    if current_element:
        count = int(current_count) if current_count else 1
        if current_element in elements:
            elements[current_element] += count
        else:
            elements[current_element] = count

    massamolar = 0
    for element_symbol, count in elements.items():
        elemento_quimico = element(element_symbol)
        peso_atomico = elemento_quimico.mass
        massamolar += peso_atomico * count
    
    questao = f"Qual é a massa molar de {formula}?"
    return questao, massamolar

# Exemplo de uso
quest, ans = QuestMaker("H2SO4")
user_resposta = "98.072"
resultado = Correcao(quest, ans, user_resposta)
print (quest)
print(resultado)
