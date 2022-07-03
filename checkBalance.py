def mol_form(compound_formula):
    """(str) -> dictionary
    When passed a string of the compound formula, returns a dictionary 
    with the elements as keys and the number of atoms of that element as values.
    
    >>> mol_form("C2H6O")
    {'C': 2, 'H': 6, 'O': 1}
    >>> mol_form("CH4")
    {'C': 1, 'H': 4}
    """
    # TODO your code here
  
    result = {}
    x = []
    while len(compound_formula) > 0:
        #print( "start "+compound_formula)
        y=""
        if compound_formula[0] == "(":
            inPar = ""
            parAndMult = ""
            Mult = ""
            endPar = compound_formula.find(")")
            if endPar + 1 == len(compound_formula) - 1:
                Mult += compound_formula[-1]
                inPar += compound_formula[1:-2]
                parAndMult += compound_formula
            elif compound_formula[endPar + 2].isnumeric():
                if endPar + 2 == len(compound_formula) - 1:
                    parAndMult +=compound_formula
                    Mult += compound_formula[-2:]
                    inPar += compound_formula[1:-3]
                else:
                    parAndMult += compound_formula[0: endPar + 3]
                    Mult += parAndMult[-2:]
                    inPar = parAndMult[1:-3]
            else:
                parAndMult += compound_formula[0: endPar + 2]
                Mult += parAndMult[-1]
                inPar += parAndMult[1:-2]            
            distributed = ""
            while len(inPar)>0:
                j = len(inPar)
                a = ""
                z = ""
                if len(inPar)==1:
                    z="1"
                    a = inPar
                    inPar = ""
                elif inPar[1].islower():
                    if len(inPar)==2:
                        z = "1"
                        a = inPar
                        inPar == ""
                    else:
                        if inPar[2].isnumeric():
                            if len(inPar)==3:
                                a =  inPar[0:2]
                                z = inPar[2]
                                inPar = ""
                            elif inPar[3].isnumeric():
                                if len(inPar)==4:
                                    a = inPar[0:2]
                                    z = inPar[2:]
                                    inPar = ""
                                else:
                                    a = inPar[0:2]
                                    z = inPar[2:4]
                                    inPar = inPar[inPar.find(a+z)+len(a+z):]
                            else:
                                a = inPar[0:2]
                                z = inPar[2]
                                inPar = inPar[inPar.find(a+z)+len(a+z):]
                        else:
                            a = inPar[0:2]
                            z ="1"
                            inPar = inPar[2:]
                elif inPar[1].isnumeric():
                    if len(inPar)==2:
                        z = inPar[1]
                        a = inPar[0]
                        inPar = ""
                    elif inPar[2].isnumeric:
                        if len(inPar)==3:
                            a = inPar[0]
                            z = inPar[1:]
                            inPar =""
                        else:
                            a = inPar[0]
                            z = inPar[1:3]
                            inPar = inPar[inPar.find(a+z)+len(a+z):]
                    else:
                        z = inPar[1]
                        a = inPar[0]
                        inPar = inPar[2:]
                else:
                    z = "1"
                    a = inPar[0]
                    inPar = inPar[1:]
                m = str(int(z)*int(Mult))
                distributed += a + m
                k = len(inPar)

            compound_formula = compound_formula[compound_formula.find(parAndMult)+len(parAndMult):]
            compound_formula = compound_formula + distributed 
        elif len(compound_formula) == 1:
            y = compound_formula[0]
            x.append(y)
            compound_formula = ""
        elif compound_formula[0].isupper() and (compound_formula[1].isupper() or compound_formula[1] == "("):
            y = compound_formula[0]
            x.append(y)
            compound_formula = compound_formula[1:]
        else:
            i = 1
            y+=compound_formula[0]
            switch = True
            while switch:
                if i > len(compound_formula)-1: #and compound_formula[i].isnumeric():
                    #y+=compound_formula[i]
                    switch = False
                elif compound_formula[i]=="(" or compound_formula[i].isupper():
                    switch = False
                elif compound_formula[i].islower():
                    if compound_formula[i].isnumeric():
                        if compound_formula[1].isnumeric():
                            y+=compound_formula[i]
                            i+=1
                        else:
                            y+=compound_formula[i]
                            i+=1
                    else:
                        y+=compound_formula[i]
                        i+=1
                else:
                    y+=compound_formula[i]
                    i+=1     
            x.append(y)
            compound_formula = compound_formula[compound_formula.find(y)+len(y):]
            #print("end "+compound_formula)
    # print(x)
    for i in x:
        if len(i) == 1:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        elif len(i) == 2:
            if i[1].isnumeric():
                if i[0] in result:
                    result[i[0]] += int(i[1])
                else:
                    result[i[0]] = int(i[1])
            else:
                if i in result:
                    result[i] += 1
                else:
                    result[i] = 1
        elif len(i) == 3:
            if i[1].isnumeric():
                if i[0] in result:
                    result[i[0]] += int(i[1:])
                else:
                    result[i[0]] = int(i[1:])
            else:
                if i[0:2] in result:
                    result[i[0:2]] += int(i[2])
                else:
                    result[i[0:2]] = int(i[2])
        else:
            if i[0:2] in result:
                result[i[0:2]] += int(i[2:])
            else:
                result[i[0:2]] = int(i[2:])
    return result

def expr_form(expr_coeffs,expr_molecs):
    """
    (tuple (of ints), tuple (of dictionaries)) -> dictionary
    
    This function accepts two input tuples that represent a chemical expression,
    or one side of a chemical equation. The first tuple contains integers that
    represent the coefficients for molecules within the expression. The second
    tuple contains dictionaries that define these molecules. The molecule
    dictionaries have the form {'atomic symbol' : number of atoms}. The order
    of the coefficients correspond to the order of molecule dictionaries.
    The function creates and returns a dictionary containing all elements within
    the expression as keys and the corresponding number of atoms for each element
    within the expression as values.
    
    For example, consider the expression 2NaCl + H2 + 5NaF
    
    >>> expr_form((2,1,5), ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1}))
    {'Na': 7, 'Cl': 2, 'H': 2, 'F': 5}
    
    """
    # TODO your code here
    elements_with_tot = {}
    for i in range(0, len(expr_coeffs)):
        for elem in expr_molecs[i]:
            key = elem
            if key in elements_with_tot:
                elements_with_tot[elem] = elements_with_tot[elem] + expr_coeffs[i]*expr_molecs[i][elem]
            else:
                elements_with_tot[elem] = expr_coeffs[i]*expr_molecs[i][elem]
    return elements_with_tot
########################################################
# PART 3 - Check if two dictionaries representing
#          the type and number of atoms on two sides of
#          a chemical equation contain different
#          key-value pairs
########################################################

def find_unbalanced_atoms(reactant_atoms, product_atoms):
    """
    (Dict,Dict) -> Set
    
    Determine if reactant_atoms and product_atoms contain equal key-value
    pairs. The keys of both dictionaries are strings representing the 
    chemical abbreviation, the value is an integer representing the number
    of atoms of that element on one side of a chemical equation.
    
    Return a set containing all the elements that are not balanced between
    the two dictionaries.
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 1, "Cl" : 2})
    {'Na'}
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 2, "Cl" : 2})
    set()
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "F" : 2, "Cl" : 2})
    {'F', 'Na'}
    """
    
    # TODO your code here
    atoms_not_balanced = {}
    atoms_not_balanced = set(atoms_not_balanced)
    for atom in reactant_atoms:  
        if atom not in product_atoms or reactant_atoms[atom] != product_atoms[atom]:
            atoms_not_balanced.add(atom)    
    for atom in product_atoms:
        if atom not in reactant_atoms or product_atoms[atom] != reactant_atoms[atom]:
            atoms_not_balanced.add(atom)     
    return atoms_not_balanced


def check_eqn_balance(reactants,products):
    """
    (tuple,tuple) -> Set
    
    Check if a chemical equation is balanced. Return any unbalanced
    elements in a set.
    
    Both inputs are nested tuples. The first element of each tuple is a tuple
    containing the coefficients for molecules in the reactant or product expression.
    The second element is a tuple containing strings of the molecules within
    the reactant or product expression. The order of the coefficients corresponds
    to the order of the molecules. The function returns a set containing any
    elements that are unbalanced in the equation.
    
    For example, the following balanced equation
    C3H8 + 5O2 <-> 4H2O + 3CO2
    
    would be input as the following two tuples:
    reactants: ((1,5), ("C3H8","O2"))
    products: ((4,3), ("H2O","CO2"))
    
    >>> check_eqn_balance(((1,5), ("C3H8","O2")),((4,3), ("H2O","CO2")))
    set()
    
    Similarly for the unbalanced equation
    
    C3H8 + 2O2 <-> 4H2O + 3CO2
    
    would be input as the following two tuples:
    reactants: ((1,2), ("C3H8","O2"))
    products: ((4,3), ("H2O","CO2"))
    
    >>> check_eqn_balance(((1,2), ("C3H8","O2")),((4,3), ("H2O","CO2")))
    {'O'}
    
    """
    
    #TODO your code here
    reactants_prime = [reactants[0]]
    reactants_prime_mol_form = []
    for i in range(0 , len(reactants[1])):
        count_of_elem_in_mole_reactants = mol_form(reactants[1][i])
        reactants_prime_mol_form.append(mol_form(reactants[1][i]))
    reactants_prime.append(tuple(reactants_prime_mol_form))
    reactants_prime = tuple(reactants_prime)
    count_atoms_of_elem_reactants = expr_form(reactants_prime[0],reactants_prime[1])
    products_prime = [products[0]]
    products_prime_mol_form = []
    for i in range(0 , len(products[1])):
        count_of_elem_in_mole_products = mol_form(products[1][i])
        products_prime_mol_form.append(mol_form(products[1][i]))
    products_prime.append(tuple(products_prime_mol_form))
    products_prime = tuple(products_prime)
    count_atoms_of_elem_products = expr_form(products_prime[0],products_prime[1])
    return find_unbalanced_atoms(count_atoms_of_elem_reactants,count_atoms_of_elem_products)