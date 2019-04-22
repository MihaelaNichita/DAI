
from itertools import permutations

# complexitate: de la 5^5 la 5!
def fete_etaje():
  for A,B,C,D,E in permutations([1,2,3,4,5]):
    if A!=5 and B!=1 and C not in [1,5] and D>B and abs(E-C)>1:
      print(f"Ana-{A}, Bianca-{B}, Carmen-{C}, Diana-{D}, Elena-{E}")

      
def fete_etaje_compact1():
  sol = []
  for A,B,C,D,E in permutations([1,2,3,4,5]):
    if A!=5 and B!=1 and C not in [1,5] and D>B and abs(E-C)>1:
      sol.append([A,B,C,D,E])
  return sol

def fete_etaje_compact2():
  sol = ((A,B,C,D,E) for (A,B,C,D,E) in permutations([1,2,3,4,5]) if A!=5 and B!=1 and C not in [1,5] and D>B and abs(E-C)>1)
  print(sol)
  return sol
  
 
def print_fete_etaje(list):
  for e in list:
    A,B,C,D,E = e
    print(f"Ana-{A}, Bianca-{B}, Carmen-{C}, Diana-{D}, Elena-{E}")





def factorial(n):
  f=1
  for x in range(6):
    f=f*(x+1)
  return f

print("Etaje Fete:")
fete_etaje()
print("5! = ",factorial(5))

sol = fete_etaje_compact2()
#print_fete_etaje(sol)





  


