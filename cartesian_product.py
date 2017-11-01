def cart_prod(*sets):
    result = [[]]
    set_list = list(sets)
    for s in set_list:
        result = [x+[y] for x in result for y in s]
    if (len(set_list) > 0):
        return {tuple(prod) for prod in result}
    else:
        return set(tuple())
