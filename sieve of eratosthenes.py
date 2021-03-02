import math

num = 20

primes = [i for i in range(2, num+1)]

i = 2

while i <= int(math.sqrt(num)):
    # if i is in list
    # then we've to delete its multiples

    if i in primes:
        # j will give multiples of i
        # starting from i*2

        for j in range(i*2, num+1, i):
            if j in primes:
                # deleting the multiples found in the list

                primes.remove(j)

    i += 1

print(primes)
