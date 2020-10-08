a = input("Masukkan bilangan A: ")
b = input("Masukkan bilangan B: ")

def hexToDec(hexInput):
    if(len(hexInput)==1):
        if(ord(hexInput)<58):
            return int(hexInput)
        else:
            return ord(hexInput)-55
    else:
        lastChar = hexInput[len(hexInput)-1]
        newHexInput = hexInput[0:len(hexInput)-1]
        return hexToDec(newHexInput)*16 + hexToDec(lastChar)

def decToHex(decInput):
    val = ""
    if(decInput>0):
        if(decInput%16<10):
            val+=str(decInput%16)
        else:
            val+= chr(decInput%16+55)
        return decToHex(decInput//16) + val
    return val

print( a + " + " + b + " = " + decToHex(hexToDec(a) + hexToDec(b)))