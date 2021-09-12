def unright(x,d):
    x = x[d:] + x[0:d]
    return x

def unleft(x,d):
    x = x[::-1]
    x = unright(x,len(x)-d)
    return x

def undown(x):
    x = ''.join(['1' if x[i] == '0' else '0' for i in range(len(x))])
    return x

def unup(x):
    t = []
    for i in range(0,len(x),8):
        decimal = 0
        for k in range(8):
            decimal += int(x[i+k])*pow(2,7-k)
        char = chr(decimal >> 1)
        t.append(char)
    return ''.join(t)

def decode(encoded):
    d = 24
    x = unleft(encoded,d)
    x = undown(x)
    x = unright(x,d)
    x = unup(x)
    return x

def main():
    encoded = "1010000011111000101010101000001010100100110110001111111010001000100000101000111011000100101111011001100011011000101011001100100010011001110110001001000010001100101111001110010011001100"
    print(decode(encoded))

if __name__ == "__main__":
    main()