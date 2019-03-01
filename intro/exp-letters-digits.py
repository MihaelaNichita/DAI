'''
puzzle 2

# Given: one letter = one unique digit in range(0,9)
    ODD + ODD = EVEN (1) -> O,D,V,N,F,R,T,Y,S,X,Y
    FORTY + TEN + TEN = SIXTY (2)
    (1) or (2) = true
# Q: Develop a program which determines the digits that should be assigned to
     each letter in order for one of the expressions (1) and (2) to be true

'''
def getNumbers1():
    for O in range(10):
        for D in range(10):
            if D!=O:
                num = exp1(O,D)
                printIfEqual1(num,O,D)


def getNumbers2():
    for F in range(10):
        for O in range(10) and O!=F:
            for R in range(10) and R not in [F,O]:
                for T in range(10) and T not in [F,O,R]:
                    for Y in range(10) and Y not in [F,O,R,T]:
                        num = exp2(F,O,R,T,Y)
                        printIfEqual2(num,F,O,R,T,Y)


def exp1(O,D):
    return 2*(O*100+D*11)

def exp2(F,O,R,T,Y,E,N):
    return F*10000+O*1000+R*100+T*10+Y+2*(T*100+E*10+N)

def printIfEqual1(num,O,D):
    N = num%10
    E = int(num/10)%10
    V = int(num/100)%10
    if E in [V,N,O,D] or N in [V,O,D] or N in [O,D] or E!=int(num/1000)%10:
        pass
    else:
        print(f"{O}{D}{D}+{O}{D}{D}={E}{V}{E}{N}")


def printIfEqual2(num,F,O,R,T,Y):
    if int(num/100000) == 0:
        return


        
getNumbers1()

