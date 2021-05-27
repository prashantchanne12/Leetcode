def swap_numbers(a, b):

    a = a ^ b
    b = a ^ b
    a = a ^ b

    return a, b


print(swap_numbers(10, 11))
