while True:
        while True:
                n = int(input("input n"))
                if n >= 0:
                        break
        i = 0
        s = 0
        while s < n:
                s = s + (i * 2)
                i = i + 1
        if s == n:
                print(n, "est pronique")
        print("k=", i-1)
