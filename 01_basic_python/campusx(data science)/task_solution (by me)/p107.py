
def gcd(a, b):
    if a == b:
        return a
    elif a>b:
        return gcd(a-b, b)
    else:
        return gcd(b-a, a)
gcd(16, 24)