def add_fract(n1,n2,d1,d2):
    if d1 == d2:
        n = n1+n2
        d = d1=d2
        print(n,"/", d)
    






use = 'y'
while use == 'y':
    n1 = int(input("input numerator 1: "))
    d1 = int(input("input demoninator 1: "))
    n2 = int(input("input numerator 2: "))
    d2 = int(input("input demoninator 2: "))
    print("enter 1 add 2 fractors\n enter 2 to subtract factions")
    ch = int(input("enter 1 add 2 fractors\n enter 2 to subtract factions"))
    if ch == 1:
        add_fract(n1,n2,d1,d2)
