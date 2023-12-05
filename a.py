def fast_power(base, power):
    """
    Returns the result of a^b i.e. a**b
    We assume that a >= 1 and b >= 0

    Remember two things!
     - Divide power by 2 and multiply base to itself (if the power is even)
     - Decrement power by 1 to make it even and then follow the first step
    """

    result = 1
    while power > 0:
        if power & 1:
            power = power - 1
            result = result * base
        power = power // 2
        base = base * base
    return result

if __name__ == '__main__':
    print(fast_power(2,3))