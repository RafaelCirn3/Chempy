from elements import elements
# adds an element to elements contained


def add_elemento(ctu):
    num_str = ""
    while int(ctu) > -1:
        num_str += compound[c - ctu]
        ctu -= 1
    repeats = int(num_str)
    while repeats > 0:
        elements_contained.append(current)
        repeats -= 1

# next two functions print the report of all the information we know


def percent_of_total(element_looking_for, total):
    times = num_of_each[element_looking_for]
    mass = round(elements[element_looking_for][1] * times, 2)
    # returns percent rounded to same number of decimal places as the other
    return (round(((mass / total) * 100), 3), mass)

# prints the report at the end


def print_report(percent_comp, total_mass):
    print("---------------------------------------------------------")
    print("| Total de massa molar: {0:<36s}|".format(
        str(total_mass) + " gramas/mol"))
    print("|{0:<55s}|".format(" "))
    print("|      {0:<49s}|".format("Percentual de Composição: "))

    for el in num_of_each.keys():
        # prints the percentage of each element and the respective mass
        (percent, mass_of_element) = percent_of_total(el, total_mass)
        if (len(num_of_each.keys()) == 1):
            # 19
            print("|          {0:<13s}- {1:0>6.2f} % {2:<15s}|".format(
                elements[el][0], percent, "(" + str(mass_of_element) + " grama)"))
        else:
            print("|          {0:<13s}- {1:0>6.3f} % {2:<15s}|".format(
                elements[el][0], percent, "(" + str(mass_of_element) + " grama)"))

    print("---------------------------------------------------------")


while True:
    # gets compound and the elements in it
    compound = input("Insira o Composto: ")
    elements_contained = []
    current = ""
    quit = False
    ct = 0
    for c in range(0, len(compound)):
        if (compound[c].isupper()):
            # if it is uppercase, indicates that we have begun to look at a new element
            current = compound[c]
            try:
                if ((not compound[c + 1].isdigit()) and (not compound[c + 1].islower())):
                    elements_contained.append(current)
            except:
                pass
        elif (compound[c].islower()):
            # if it's lower, add it to the existing element we're looking at
            current += compound[c]
            try:
                if (compound[c + 1].isupper()):
                    elements_contained.append(current)
            except:
                pass
        elif (compound[c].isdigit()):
            try:
                if (compound[c + 1].isdigit()):
                    # if there are more digits to the subscript then it counts that and moves on
                    ct += 1
                    continue
                else:
                    # gets a string with a number that represents the coefficient no matter how many digits it has
                    add_elemento(ct)
                    ct = 0
            except:
                # means we're at the end of the number, so it appends it
                add_element(ct)
                ct = 0
        else:
            # prints invalid if it finds something that is a symbol like a $ or a #
            print("Composto inválido:", compound[c])
            quit = True
            break
        # If it's the end of the compound, adds the final element the appropriate number of times
        if ((c == len(compound) - 1) and not compound[c].isdigit()):
            elements_contained.append(current)

    molar_mass = 0
    num_of_each = {}
    # goes through each item in there and adds it to the total
    if (not quit):
        for ele in elements_contained:
            if (ele in elements):
                molar_mass += elements[ele][1]
                if (ele in num_of_each):
                    num_of_each[ele] += 1
                else:
                    num_of_each.update({ele: 1})
            else:
                print("Elemento Inválido:", ele)
                quit = True
                break

    if (not quit):
        num_places = input(
            "Quantas casas decimais a resposta final deve ser arredondada (zeros extras serão removidos)? ")
        try:
            num_places = int(num_places)
        except:
            print("Número inválido, utilizando 3 como padrão.")
            num_places = 3

        molar_mass = round(molar_mass, num_places)
        print("")  # blank line for clarity
        print_report(num_of_each, molar_mass)

    print("")
    go_again = input("Calcular outro ? (s/n)? ").lower()
    if (go_again != "sim" and go_again != "s"):
        print("\nObrigado por utilizar nosso sistema\nCangaçoDev")
        break
    else:
        print("\n-----------------------------------------------------------------------------------------\n")
        continue
