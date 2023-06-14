while True:
        while True:
                n = input("input a number")
                if int(n) > 1:
                        break
        n1 = n
        t = 0
        print(n)
        while True:
                i = 1
                s = 0
                while True:
                        if int(n) % int(i) == 0:
                                s = int(s) + int(i)
                        i = int(i) + int(1)
                        if int(i) >  int(n)/int(2):
                                break
                t = int(t) + int(1)
                print(s)
                n = s
                if int(s) == 1 or int(s) == int(n1):
                        break
        print("t = " + str(t))
        if int(s) == 1 and int(t) == 1:
                print(str(n1) + " est un nombre premier")
        if int(s) == int(n1) and int(t) == 1:
                print(str(n1) + " est un nombre parfait ")
        elif int(s) == int(n1) and int(t) == 2:
                print(str(n1) + " est un nombre amical ")
        elif int(s) == int(n1):
                print(str(n1) + " est un nombre sociable d'ordre " + str(t))


                        
                
