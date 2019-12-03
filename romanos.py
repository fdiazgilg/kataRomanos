valores = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
valores5 = {'V':5, 'L':50, 'D':500}
simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

#Definimos estas tuplas para la transformacion de arabigo a romano
romanTipo1 = ('M', 'C', 'X', 'I')
romanTipo5 = ('D', 'L', 'V')

def numParentesis(cadena):
    num = 0
    for c in cadena:
        if c == '(':
            num += 1
        else:
            break
    return num

def contarParentesis(numRomano):
    res = []
    grupoParentesis = numRomano.split(')')

    ix = 0
    while ix < len(grupoParentesis):
        grupo = grupoParentesis[ix]
        numP = numParentesis(grupo)
        if numP > 0:
            for j in range(ix+1, numP):
                if grupoParentesis[j] != '':
                    return 0
            res.append([numP, grupo[numP:]])
            ix += numP
        #Este else lo creamos para añadir el ultimo elemento que no lleva parentesis numP = 0
        else:
            ix += 1
            if grupo != '':
                res.append([0,grupo])
        
        #Este if sirve para tratar los casos de parentesis mal formateados
        if len(res) > 1:
            for i in range(len(res)-1):
                if res[i][0] <= res[i+1][0]:
                    return 0

    return res


def romano_a_arabigo(numRomano):
    numArabigoTotal = 0
    res = contarParentesis(numRomano)

    for i in range(len(res)):
        numArabigo = 0
        numRepes = 1
        ultimoCaracter = ''
        numRomano = res[i][1]
        factor = pow(10,3*res[i][0])

        for letra in numRomano: 
            #incrementamos el valor del número arábigo con el valor numérico del símbolo romano
            if letra in valores:
                numArabigo += valores[letra]
                if ultimoCaracter == '':
                    pass
                elif valores[ultimoCaracter] > valores[letra]:
                    numRepes = 1
                elif valores[ultimoCaracter] == valores[letra]:
                    numRepes += 1
                    if letra in valores5:
                        return 0
                    if numRepes > 3:
                        return 0
                elif valores[ultimoCaracter] < valores[letra]:
                    if numRepes > 1: # No permite repeticiones en las restas
                        return 0
                    if ultimoCaracter in valores5: #No permite restas de valores de 5 (5, 50, 500)
                        return 0
                    distancia = simbolosOrdenados.index(letra) - simbolosOrdenados.index(ultimoCaracter) #No permite que se resten unidades de más de un orden
                    if distancia > 2:
                        return 0
                    numArabigo -= valores[ultimoCaracter]*2
                    numRepes = 1
            else:  #si el simbolo romano no es permitido devolvemos error (0)
                return 0

            ultimoCaracter = letra

        numArabigoTotal += numArabigo * factor

    return numArabigoTotal


def arabigo_a_romano(valor):
    #Variables para el resultado, separar el arabigo y la traduccion a romano de la separacion del arabigo
    numRomano = ''
    
    #Si es menor que 0 o mayor que 3999 retornamos 0
    if valor > 3999 or valor <= 0:
        return 0
    else:
        cad = str(valor)

    #Recorremos la lista para su transformacion en romanos
    for i in range(-len(cad), 0):
        if cad[i] <= '3':
            numRomano += int(cad[i]) * romanTipo1[i]
        elif cad[i] == '4':
            numRomano += romanTipo1[i]+romanTipo5[i]
        elif cad[i] < '9':
            numRomano += romanTipo5[i] + (int(cad[i])-5) * romanTipo1[i]
        else:
            numRomano += romanTipo1[i]+romanTipo1[i-1]
    
    return numRomano
