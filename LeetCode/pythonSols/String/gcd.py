def gcd(a, b):
    """
    Compute gcd of 2 nums
    """
    if a==0 or b==0:
        return 0
    while a!=b :
        if a>b :
            a = a-b
        elif b>a : 
            b = b-a
    return a


if __name__ == '__main__':
    print gcd(0, 10)