valores = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
valores5 = {'V':5, 'L':50, 'D':500}
simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

#Definimos estas tuplas para la transformacion de arabigo a romano
romanTipo1 = ('M', 'C', 'X', 'I')
romanTipo5 = ('D', 'L', 'V')

def romano_a_arabigo(numRomano):
    #Separamos el romano por los parentesis finales y creamos acumulador Total
    romanSep = numRomano.split(')')
    numArabigoTotal = 0

    #Nuevo bucle para transformar en romano cada elemento de romanSep
    for romano in romanSep:
        #Variables factor y countParent para conocer por que numero multiplicamos
        countParent = 0
        factor = 1
        numArabigo = 0
        ultimoCaracter = ''
        numRepes = 1

        for letra in romano:
            if letra == '(':
                countParent += 1
                factor = pow(10,3*countParent)
            elif letra in valores:
                numArabigo += valores[letra]
                if ultimoCaracter == '':
                    pass
                elif valores[letra] < valores[ultimoCaracter]:
                    numRepes = 1
                elif valores[letra] == valores[ultimoCaracter]:
                    numRepes += 1
                    if letra in valores5 or numRepes > 3:
                        return 0
                elif valores[letra] > valores[ultimoCaracter]:
                    if ultimoCaracter in valores5 or numRepes > 1:
                        return 0
                    distancia = simbolosOrdenados.index(letra) - simbolosOrdenados.index(ultimoCaracter)
                    if distancia > 2:
                        return 0
                    numArabigo -= valores[ultimoCaracter] * 2
                    numRepes = 1
                else:
                    return 0
            else:
                return 0

            if letra == '(' or letra == ')':
                ultimoCaracter = ''
            else:
                ultimoCaracter = letra
        numArabigoTotal += numArabigo * factor

    return numArabigoTotal


def arabigo_a_romano(valor):
    #Variables para el resultado, separar el arabigo y la traduccion a romano de la separacion del arabigo
    numRomano = ''
    valorSep = []
    listNumRomano = []
    
    #Si es menor que 0 o mayor que 3999 retornamos 0
    if valor > 3999 or valor <= 0:
        return 0
    else:
        #Separamos el arabigo en millares, centenas, decenas y unidades
        millares = valor // 1000
        centenas = (valor % 1000) // 100
        decenas  = ((valor % 1000) % 100 ) // 10
        unidades = ((valor % 1000) % 100) % 10
        #Almacenamos cada elemento en la variable valorSep
        valorSep.append(millares)
        valorSep.append(centenas)
        valorSep.append(decenas)
        valorSep.append(unidades)

    #Recorremos la lista para su transformacion en romanos
    for i in range(-len(valorSep), 0):
        if valorSep[i] <= 3:
            listNumRomano.append(valorSep[i] * romanTipo1[i])
        elif valorSep[i] == 4:
            listNumRomano.append(romanTipo1[i]+romanTipo5[i])
        elif valorSep[i] <= 8 and valor >= 5:
            listNumRomano.append(romanTipo5[i] + (valorSep[i]-5) * romanTipo1[i])
        else:
            listNumRomano.append(romanTipo1[i]+romanTipo1[i-1])
    
    #Recorremos la lista generada en el paso anterior y sumamos para obtener el resultado final
    for j in range(len(listNumRomano)):
        numRomano += listNumRomano[j]
    
    return numRomano
