
valores = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
valores5 = {'V':5, 'L':50, 'D':500}
simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

def romano_a_arabigo(numRomano):
    numArabigo = 0
    numRepes = 1
    ultimoCaracter = ''


    for letra in numRomano:

        if letra in valores:
            if ultimoCaracter == '':
                pass
            elif valores[letra] < valores[ultimoCaracter]:
                numRepes = 1
                numArabigo += valores[ultimoCaracter]
            elif valores[letra] == valores[ultimoCaracter]:

                numArabigo += valores[ultimoCaracter]
                numRepes += 1

                if letra in valores5:
                    return 0
                if numRepes > 3:
                    return 0
            elif valores[letra] > valores[ultimoCaracter]:
                if numRepes > 1:
                    return 0

                if ultimoCaracter in valores5:
                    return 0

                distancia = simbolosOrdenados.index(letra) - simbolosOrdenados.index(ultimoCaracter)
                if distancia > 2:
                    return 0

                numArabigo -= valores[ultimoCaracter]
                numRepes = 1

            else:
                return 0
        else:
            return 0

        ultimoCaracter = letra

    numArabigo += valores[letra]

    return numArabigo
