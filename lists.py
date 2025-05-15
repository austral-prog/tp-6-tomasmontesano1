def remove_elements(list_to_remove_elements):
    l1 = list_to_remove_elements
    l2 = len(l1)
    if l2 >= 6:
        del l1[5]
    l2 = len(l1)
    if l2 >= 5:
        del l1[4]
    l2 = len(l1)
    if l2 >= 1:
        del l1[0]
    return l1
# Remove this line and implement


def add_elements(list_to_add_elements):
    list_to_add_elements.append('Yellow')
    list_to_add_elements.insert(0,'Pink')



    return list_to_add_elements  # Remove this line and implement


def is_empty(list_to_check):
    a=[]
    if list_to_check==a:
        return True
    else:
        return False




    # Remove this line and implement


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)>2 and len(list_to_compare2)>2 and list_to_compare1[2]==list_to_compare2[2]:
        return True
    else:
        return False

def list_of_lists(list_of_lists_to_modify):
    lista = list_of_lists_to_modify
    l1 = lista[0]
    l2 = lista[1]
    l3 = lista[2]
    l1 = l1[0:2]
    l2 = l2[1:4]
    longitud = len(l3)
    l3 = l3[longitud-2:longitud]
    lista =[l1,l2,l3]
    return lista

