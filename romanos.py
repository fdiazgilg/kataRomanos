
valores = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
valores5 = {'V':5, 'L':50, 'D':500}

def romano_a_arabigo(numRomano):
    numArabigo = 0
    numRepes = 1
    ultimoCaracter = ''

    for letra in numRomano:
        if letra == ultimoCaracter:
            numRepes += 1
        else:
            numRepes = 1
        if numRepes > 3:
            return 0
        
 
        if letra in valores:
            if ultimoCaracter == '':
                pass
            elif valores[letra] <= valores[ultimoCaracter]:
                numArabigo += valores[ultimoCaracter]
            elif ultimoCaracter not in valores5:
                numArabigo -= valores[ultimoCaracter]
            else:
                return 0
        else:
            return 0

        ultimoCaracter = letra

    numArabigo += valores[letra]

    return numArabigo
