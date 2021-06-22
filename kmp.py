
def init_arr(pattern):

    i = 0
    j = 1

    arr = [0 for x in range(len(pattern))]
    arr[0] = 0

    while j < len(pattern):

        if pattern[i] == pattern[j]:
            i += 1
            arr[j] = i
            j += 1

        # first character did not match
        elif i == 0:
            arr[j] = 0
            j += 1

        # Mismatch after at least one matching character:
        else:
            i = arr[i-1]

    print(arr)

    return arr


def kmp_search(string, pattern):

    prefix_arr = init_arr(pattern)

    i = 0
    j = 0

    while i < len(pattern) and j < len(string):

        # last character matches
        if pattern[i] == string[j] and i == len(pattern) - 1:
            return True

        # character mayches
        elif pattern[i] == string[j]:
            i += 1
            j += 1

        # character did not match
        else:
            if i != 0:
                i = prefix_arr[i-1]
            else:
                j += 1

    return False


print(kmp_search('abaxabab', 'abab'))
