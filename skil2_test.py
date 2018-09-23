from skil2_foll import *
# spyr um nafn
nafn = input('Hvað heitr þú?: ')
now = time.localtime()
# while loop fyrir aðalvalmynd
while True:
    # valmynd
    menu()
    # fyrir hvert val er reynt að keyra fall. ef það virkar ekki, eða notandi slær inn vitlaust,
    # er birt 'Villa!', eða eitthvað álíka
    try:
        #tekur inn tölu
        val = int(input(': '))
        # val 1
        if val == 1:
            # Fyrir flest val er keyt annað while loop þar sem forrit er keyrt þar til notandi velur að hætta
            while True:
                try:
                    #tekur inn tölu
                    a = int(input('hlið a(-tala til að hætta):  '))
                    #ef tala er stærri en -1 er haldið áfram, annars er while loop stoppuð
                    if a > -1:
                        b = int(input('hlið b: '))
                        langhlid(a,b)
                    else:
                        break
                #ef það kemur upp villa er byty 'Villa'
                except:
                    print('Villa')
        elif val == 2:
            while True:
                try:
                    print('(0 til að hætta)')
                    a = int(input('Fyrri tala: '))
                    #ef fyrri tala er ekki 0 þá er keyrt áfram, annar er while loop stoppuð
                    if a != 0:
                        b = int(input('Seinni tala: '))
                        margfeldiAf(a,b)
                    else:
                        break
                except:
                    print('villa')
        elif val == 3:
            try:
                a = int(input('Stærð á kassa: '))
                stjornuKassi(a)
            except:
                print('villa')
        elif val == 4:
            while True:
                try:
                    print('0 til að hætta: ')
                    a = int(input('Er tala slétt?: '))
                    if a != 0:
                        slettTala(a)
                    else:
                        break
                except:
                    print('Villa!')
        elif val == 5:
            while True:
                try:
                    print('(-tala til að hætta)')
                    a = int(input('Radíus: '))
                    if a > -1:
                        flatarmalHrings(a)
                    else:
                        break
                except:
                    print('Villa')
        elif val == 6:
                try:
                    #tekur inn sekúndur of keyrir fall
                    a = int(input('Sekúndur...'))
                    bank(a)
                except:
                    print('Villa!')

        elif val == 7:
            #Notandi velur að hætta. þá er hann kvaddur með nafni og hvað klukkan er
            print ('Vertu sæl/l,', nafn)
            print('Klukkan er %s:%s'%(now[3],now[4]))
            break
        else:
            print('Röng tala')
    #villa kom upp við valmynd
    except:
        print('Villa. Sláðu inn tölu')
