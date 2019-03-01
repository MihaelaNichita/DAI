'''
Puzzle 1:

Given: A block with 5 floor. There is a girl at each floor:
    1. Ana doesn't stay at the last floor;
    2. Bianca doesn't stay at the first floor;
    3. Christina noesn't stay at any of the first and the last floor;
    4. Diana stays above Bianca (one or more flats between them);
    5. Elena doesn't stay at a floor that is adjacent to Christina's floor.

Q: Where does each of the girls stay? How many solutions are there?

'''

def get_floors():
    i=0
    for A in range(1,5):
        for B in range(2,5):
            if B!=A:
                for C in range(2,5):
                    if B!=C and C!=A:
                        for D in range(B,6):
                            if D!=A and D!=B and D!=C:
                                for E in range(1,6):
                                    if E not in [A,B,C,D] and abs(E-C)>1:
                                        print(f"Ana - {A}, Bianca - {B}, Christina - {C}, Diana - {D}, Elena - {E}")
                                        i=i+1
    return i

    
print(f"Number of solutions: {get_floors()}")


