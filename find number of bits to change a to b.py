def find_number_of_bits(a, b):

    count = 0

    # from XORing we will get the number of
    # bits that are differnt (in the form of 1)
    n = a ^ b

    # n & (n-1) converts the least significant set bit to 0
    # count the number of ones
    while n != 0:
        n = n & (n-1)
        count += 1

    return count
