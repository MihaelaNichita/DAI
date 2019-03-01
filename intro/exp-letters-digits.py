'''
puzzle 2

# Given: one letter = one unique digit in range(0,9)
    ODD + ODD = EVEN (1) -> O,D,V,N,F,R,T,Y,S,X,Y
    FORTY + TEN + TEN = SIXTY (2)
    (1) or (2) = true
# Q: Develop a program which determines the digits that should be assigned to
     each letter in order for one of the expressions (1) and (2) to be true

'''
def getNumbers():
    for O in range(10):
        for D in range(10):
            if D!=O:
                num = expS(O,D)
                printIfEqual(num,O,D)


def expS(O,D):
    return 2*(O*100+D*11)


def printIfEqual(num,O,D):
    N = num%10
    E = int(num/10)%10
    V = int(num/100)%10
    if E==V or E==N or V==N or E!=int(num/1000)%10:
        pass
    else:
        print(f"{O}{D}{D}+{O}{D}{D}={E}{V}{E}{N}")
        
getNumbers()

