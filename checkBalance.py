#####################################################
# APS106 Winter 2022 - Lab 7 - Chemical Eqn Checker #
#####################################################

######################################################
# PART 1 - Complete the function below to deocompose
#          a compound formula written as a string
#          in a dictionary
######################################################

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
    i = 0
    result = {}
    while i < len(compound_formula):
        if compound_formula[i] in result:
            if compound_formula[i].isupper():
                if i == len(compound_formula)-1:
                    result[compound_formula[i]]+=1
                    i+=1
                elif compound_formula[i].isnumeric():
                    if i + 1 == len(compound_formula)-1:
                        result[compound_formula[i]] += int(compound_formula[i+1])
                        i+=2
                    else:
                        if compound_formula[i+2].isnumeric():
                            result[compound_formula[i]] += int(compound_formula[i+1]+compound_formula[i+2])
                            i+=3
                        else:
                            result[compound_formula[i]] += int(compound_formula[i+1])
                            i+=2
                elif compound_formula[i].isnumeric() == False:
                    if compound_formula[i].islower():
                        if i+1 == len(compound_formula)-1:
                            result[compound_formula[i]] += 1
                            i+=2
                        elif compound_formula[i+2].isnumeric() == False:
                            result[compound_formula[i]] += 1
                            i+=2
                        elif compound_formula[i+2].isnumeric():
                            if i+2 == len(compound_formula)-1:
                                result[compound_formula[i]] += int(compound_formula[i+2])
                                i+=3
                            elif compound_formula[i+3].isnumeric() == False:
                                result[compound_formula[i]] += int(compound_formula[i+2])
                                i+=3
                            elif compound_formula[i+3].isnumeric():
                                result[compound_formula[i]] += int(compound_formula[i+2]+compound_formula[i+3])
                                i+=4
                    elif compound_formula[i+1].isupper():
                        result[compound_formula[i]] += 1
                        i+=1          
        else: 
            if compound_formula[i].isupper():
                if i == len(compound_formula)-1:
                    result[compound_formula[i]]=1
                    i+=1
                elif compound_formula[i+1].isnumeric():
                    if i + 1 == len(compound_formula)-1:
                        result[compound_formula[i]] = int(compound_formula[i+1])
                        i+=2
                    else:
                        if compound_formula[i+2].isnumeric():
                            result[compound_formula[i]] = int(compound_formula[i+1]+compound_formula[i+2])
                            i+=3
                        else:
                            result[compound_formula[i]] = int(compound_formula[i+1])
                            i+=2
                elif compound_formula[i+1].isnumeric() == False:
                    if compound_formula[i+1].islower():
                        if i+1 == len(compound_formula)-1:
                            result[compound_formula[i]+compound_formula[i+1]] = 1
                            i+=2
                        elif compound_formula[i+2].isnumeric() == False:
                            result[compound_formula[i]+compound_formula[i+1]] = 1
                            i+=2
                        elif compound_formula[i+2].isnumeric():
                            if i+2 == len(compound_formula)-1:
                                result[compound_formula[i]+compound_formula[i+1]] = int(compound_formula[i+2])
                                i+=3
                            elif compound_formula[i+3].isnumeric() == False:
                                result[compound_formula[i]+compound_formula[i+1]] = int(compound_formula[i+2])
                                i+=3
                            elif compound_formula[i+3].isnumeric():
                                result[compound_formula[i]+compound_formula[i+1]] = int(compound_formula[i+2]+compound_formula[i+3])
                                i+=4
                    elif compound_formula[i+1].isupper():
                        result[compound_formula[i]] = 1
                        i+=1          
    return result

######################################################
# PART 2 - Complete the function below that takes two 
#          tuples representing one side of a
#          chemical equation and returns a dictionary
#          with the elements as keys and the total
#          number of atoms in the entire expression
#          as values.
######################################################
    
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

########################################################
# PART 4 - Check if a chemical equation represented by
#          two nested tuples is balanced
########################################################

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