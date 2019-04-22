
# Laborator 5 -  Metode de cautare
#     Problema 8-puzzle
#     cautarea greedy, A* : estimari H1, H2

import sys
from collections import namedtuple


DJOC = 3 # dimensiune joc: 3x3
Nod = namedtuple("Nod", ['stare', 'actiuni', 'd', 'g', 'h', 'f'])

def fakeSwap(stare,i1,i2):
  l = list(stare)
  temp = l[i1]
  l[i1]=l[i2]
  l[i2]=temp
  return tuple(l)


def actUp(stare):
  "*** TODO 0: mutare Sus***"
  """ Daca actiunea este aplicabila in starea data, 
        se returneaza starea urmatoare + id-ul actiunii; 
        de exemplu ((1,2,...), 'U') """ 
  if 0 not in stare[6:9]:
    i = stare.index(0)
    return fakeSwap(stare,i,i+3), 'U'
  return None

  
def actLeft(stare):
  "*** TODO 1: mutare la stanga ***"
  if 0 not in stare[2:9:3]:
    i = stare.index(0)
    return fakeSwap(stare,i,i+1), 'L'
  return None

  
def actRight(stare):
  "*** TODO 2: mutare la dreapta ***"
  if 0 not in stare[0:7:3]:
    i = stare.index(0)
    return fakeSwap(stare,i,i-1) , 'R'
  return None
 

def actDown(stare):
  "*** TODO 3: mutare jos *** "
  if 0 not in stare[0:3]:
    i = stare.index(0)
    return fakeSwap(stare,i,i-3), 'D'
  return None


def exp(stare):
    stari=[]
    "*** TODO 4: dand o stare, se returneza toate starile in care se poate ajunge ***"
    u=actUp(stare)
    l=actLeft(stare)
    r=actRight(stare)
    d=actDown(stare)

    stari=[s for s in (u,l,r,d) if s is not None]
    return stari  

    
# cautare in largime
def sect_dupa_largime(frontiera):
    nod = frontiera[0]
    del frontiera[0]
    return nod
    
# cautare in adancime
def sect_dupa_adancime(frontiera):
    nod = frontiera[-1]
    del frontiera[-1]
    return nod
 
def cautare(nod_init, sf, sect_dupa):
  "*** TODO 5: completati procedura de cautare ****"
  """ se foloseste codul de la problema de navigare (cu orare) """
  front = [nod_init]

  count=0
  while len(front)>0:  
    print(f"frontiera = {front}")     
    nod = sect_dupa(front)
    count+=1
      
    if nod.stare == sf:
      print (f'Solutia data in {count} pasi este: {nod.actiuni}')
      return
            
    stari_urmatoare = exp(nod.stare)
        
    for s,actiune in stari_urmatoare:
      "***if s not in stari anterioare:***"
        #print (s,actiune)
      g=nod.g+1
      h= h1(s,sf)
      nod_next = Nod(s, nod.actiuni + (actiune,), nod.d+1, g, h, h-g)
      front.append(nod_next)

# care este costul? 
def sect_dupa_min(front):
    index_min = 0
    nod_min = min(front,key=lambda nod:nod.g)
    index_min = front.index(nod_min)
    #print (f"Nodul cu cost minim: {nod_min}")
    return front.pop(index_min)
    
def sect_dupa_greedy(front):
    index=0
    nod_h_min = min(front, key=lambda nod:nod.h)
    index = front.index(nod_h_min)
    print (f"Nodul cu f=h minim: {nod_h_min}")
    return front.pop(index)
    
def sect_dupa_A(front):
    index=0
    nod_h_min = min(front, key=lambda nod:nod.f)
    index = front.index(nod_h_min)
    print (f"Nodul cu f=h minim: {nod_h_min}")
    return front.pop(index)

def h1(s, sf):
  "*** TODO 6: implementare functie de estimare ****"
  contor = 0
  ## returneaza numarul de piese incorect pozitionate 
  contor=len([e for e in range(1,9) if s[e] is not sf[e]])
  return contor
  
def h2(s, sf):
    "*** TODO 7: implementare functie de estimare ****"
    contor = 0
    ## suma distantelor pentru pozitionare corecta

    return 0
 


si = (1,2,3,4,0,5,6,7,8)
sf = (1,2,3,4,5,8,0,6,7)
sf2 = (1,2,3,4,5,6,7,8,0)
nod_initial = Nod(si, (), 0, 0, 0, 0)
print(nod_initial)

cautare(nod_initial,sf2, sect_dupa_A)



