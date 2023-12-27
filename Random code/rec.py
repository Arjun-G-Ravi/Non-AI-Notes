def dec2bin(n):
    if n//2 == 0:
        return str(n%2)
    
    return dec2bin(n//2) + str(n%2)

dec2bin(10)