def encode(strings):

    res = ''

    for string in strings:
        res += str(len(string))+'#'+string

    return res


def decode(string):

    res = []
    i = 0

    while i < len(string):
        # find delimiter '#'
        j = i

        while string[j] != '#':
            j += 1

        length = int(string[i:j])

        res.append(string[j+1: j+1+length])

        i = j + 1 + length

    return res


string = encode(['Pras123#hant', 'Cha12#nne'])
print(decode(string))
