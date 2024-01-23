# algoritmo, dato un numero, ne mostri la sua rappresentazione a lettere in italiano
# es 1234= output milleduecentotrentaquatro

# per i primi venti numeri - tabella
# 
def translate_to_20(n):
    if n > 19:
        return 'out of range'
    NUMBERS = ['', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici', 'dodici', 'tredici', 'quattordici', 'Quindici', 'sedici', 'diciasette', 'Diciotto', 'dicianove']
    return NUMBERS[n-1]
#dal 20 fino a 100
def translate_to_100(n):
    if n >99:
        return 'out of range'
    DECADES = ['venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta',
              'settanta', 'ottanta', 'novanta']
    decade = n//10 #la decina
    unit = n % 10 #unita da n
    return DECADES[decade -2] + translate_to_20(unit)
    
    
for x in range(1,100):
    print(translate_to_100(x))
    

