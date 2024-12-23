def multiply_numbers(seq):
    if len(seq) == 0:
        return 1
    total = 1
    for item in seq:
        if type(item) == type(10) or type(item) == type(10.01):
            total *= item
        elif type(item) == type('hello'):
            total = total * 1
        else:
            total *= multiply_numbers(item)
    return total