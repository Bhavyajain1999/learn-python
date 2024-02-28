decimal = 5

def decToBin(decimal):
    if decimal == 0:
        return "0"
    else:
        return decToBin(decimal >> 1) + str(decimal & 1)
decToBin(decimal)