#cislo = int('abc')
print('ahoj')
if 1 < 2:
    #print(1/'1')
    print(3)
vstup = input('Zadej cislo: ')
try:
    cislo = int(vstup)
    vysledek = 100 / cislo
except ValueError:
    print('Zadala jsi blbost.')
except ZeroDivisionError:
    print('Nemuzes zadat 0.')
