def numeros():
    import random as rd
    
    valor = 'Valor repetido'
    
    while valor == 'Valor repetido':
        tamanho = 0
        lista = []
        while tamanho < 6:
            lista.append(rd.randint(1,60))
            tamanho += 1 

        if lista.count(lista[0]) >= 2:            
            valor = 'Valor repetido'
        elif lista.count(lista[1]) >= 2:
            valor = 'Valor repetido'            
        elif lista.count(lista[2]) >= 2:
            valor = 'Valor repetido'            
        elif lista.count(lista[3]) >= 2:
            valor = 'Valor repetido'           
        elif lista.count(lista[4]) >= 2:
            valor = 'Valor repetido'            
        elif lista.count(lista[5]) >= 2:
            valor = 'Valor repetido'            
        else:
            valor = 'Ok'
            print(sorted(lista)) 
            break
   
numeros()