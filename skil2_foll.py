import sys, math, time
# Fall sem byrtir alla valmöguleika forritsins
def menu():
    print("1. Langhlið")
    print("2. Finna margfeldi af")
    print("3. Ferningur úr stjörnum")
    print("4. Slétt tala")
    print("5. Flatramál hrings")
    print("6. Bank, bank, hver er þar?")
    print("7. Hætta")
# fall tekur inn a og b hliðar á rétthyrndum þríhyrning og reiknar langhlið með pythogaras formúlinni
def langhlid(num1, num2):
    c = round(math.sqrt(pow(num1,2)+pow(num2,2)))
    print(c)

def margfeldiAf(a,b):
    # ef afgangurinn af b deilt með a er núll þá er a margfeldi af b, annars ekki
    if b % a == 0:
        print( a, ' er margfeldi af ', b)
    elif b % a != 0:
        print(a, ' er ekki margfeldi af ', b)


def stjornuKassi(k):
    # fyrir töluna sem sleginn er inn þá er margfaldað '*' með tölunni, sett í breytu og svo birt breytuna jafn oft og talan er stór
    for x in range(k):
        lina = '*' * k
        print(lina)
    return

def slettTala(a):
    # ef afgangur tölunnar deilt með 2 er núll þá er tala slétt, annars ekki
    if a % 2 == 0:
        print('Slétt!')
    else:
        print('Oddatala!')

def flatarmalHrings(a):
    # tekur inn radíus af hring og reiknar flatarmál hrings með viðeigandi formúlu
    f = math.pi * pow(a,2)
    print(f)

def bank(s):
    # breyta tekur inn sekúndur og gerir ráð fyrir því að það mun bætast við tími vegna 0.2 sekúnda millibilinu
    # milli hvers 'bank', þannig sá tími er mínusaður af
    tend = time.time() + s - (0.2*s)
    # prentar út 'bank' í jafn margar sekúnur og notandi slær inn
    while time.time()<tend:
        print('Bank')
        time.sleep(.2)
    print('Hver er þar?')






