from flask import Flask, request, jsonify
from elements import elements

app = Flask(__name__)

# Função para adicionar elementos ao composto conforme o coeficiente
def add_elemento(compound, current, ctu):
    num_str = ""
    # Constrói o número a partir dos dígitos no composto
    while int(ctu) > -1:
        num_str += compound[-ctu-1]
        ctu -= 1
    repeats = int(num_str)  # Converte o número para inteiro
    elements_contained = []
    # Adiciona o elemento atual à lista o número de vezes especificado
    while repeats > 0:
        elements_contained.append(current)
        repeats -= 1
    return elements_contained

# Função para calcular a porcentagem da massa molar total para um elemento específico
def percent_of_total(element_looking_for, total, num_of_each):
    times = num_of_each[element_looking_for]
    mass = round(elements[element_looking_for][1] * times, 2)
    # Retorna a porcentagem da massa total e a massa do elemento
    return (round(((mass / total) * 100), 3), mass)

# Função para analisar o composto químico e calcular a massa molar total e a quantidade de cada elemento
def calculate_molar_mass(compound):
    elements_contained = []
    current = ""
    ct = 0
    num_of_each = {}
    
    # Itera sobre cada caractere do composto
    for c in range(0, len(compound)):
        if compound[c].isupper():
            current = compound[c]
            try:
                if (not compound[c + 1].isdigit()) and (not compound[c + 1].islower()):
                    elements_contained.append(current)
            except IndexError:
                elements_contained.append(current)
        elif compound[c].islower():
            current += compound[c]
            try:
                if compound[c + 1].isupper():
                    elements_contained.append(current)
            except IndexError:
                elements_contained.append(current)
        elif compound[c].isdigit():
            try:
                if compound[c + 1].isdigit():
                    ct += 1
                    continue
                else:
                    elements_contained.extend(add_elemento(compound, current, ct))
                    ct = 0
            except IndexError:
                elements_contained.extend(add_elemento(compound, current, ct))
                ct = 0
        else:
            return "Invalid character found: {}".format(compound[c]), None
    
    molar_mass = 0
    # Calcula a massa molar total e a quantidade de cada elemento
    for ele in elements_contained:
        if ele in elements:
            molar_mass += elements[ele][1]
            if ele in num_of_each:
                num_of_each[ele] += 1
            else:
                num_of_each[ele] = 1
        else:
            return "Invalid element found: {}".format(ele), None
    
    return molar_mass, num_of_each

# Rota para calcular a massa molar e a composição percentual
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    compound = data.get('compound')
    decimal_places = data.get('decimal_places', 3)
    
    # Chama a função para calcular a massa molar e a composição do composto
    molar_mass, num_of_each = calculate_molar_mass(compound)
    if not num_of_each:
        return jsonify({"error": molar_mass}), 400
    
    molar_mass = round(molar_mass, decimal_places)
    percent_comp = {}
    
    # Calcula a composição percentual para cada elemento
    for el in num_of_each.keys():
        percent, mass_of_element = percent_of_total(el, molar_mass, num_of_each)
        percent_comp[elements[el][0]] = {
            "percent": percent,
            "mass": mass_of_element
        }
    
    return jsonify({
        "molar_mass": molar_mass,
        "percent_composition": percent_comp
    })

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
