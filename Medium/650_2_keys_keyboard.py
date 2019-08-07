def minSteps(n):
    if n == 1:
        return 0
    return sum(generate_prime_factors(n))


def generate_prime_factors(number):
    result, i = [], 2

    while i <= int(pow(number, 0.5)):

        if number % i == 0:
            result.append(i)
            number /= i
            i = 2
        else:
            i += 1

    result.append(number)
    return result


for i in range(15):
    print(i, ":", int(minSteps(i)))

print(minSteps(47))
print(minSteps(46))
print(minSteps(48))