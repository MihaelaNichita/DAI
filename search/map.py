# Laborator 3 - Metode de cautare
#     cautare in adancime, largime, de cost minim, cautare increment

import sys
from collections import namedtuple

Drum = namedtuple("Drum", ['A', 'B', 'dist'])
# fiecare nod contine: stare (oras), predecesori (orasele predecesoare), 
#    d (adancimea), g (costul caii de la nodul de start pana la nodul curent) 
Nod = namedtuple("Nod", ['stare', 'predecesori', 'd', 'g'])


drumuri = []

def citire_date_din_fisier(fisier):
  input_data = ""
  with open(fisier, 'r') as f:
       input_data = f.read().split('\n')

  linie = input_data[0].split()
  numar_orase = int(linie[0])
  numar_drumuri = int(linie[1])
  drumuri = []

  for i in range(1, numar_drumuri+1):
    linie = input_data[i].split()
    drumuri.append(Drum(linie[0],linie[1], int(linie[2])))
    
  return numar_orase, drumuri
  
def getVecini(oras):
  global drumuri
  vecini = []
  for drum in drumuri:
    if drum.A == oras:
      vecini.append(drum.B)
    if drum.B == oras:
      vecini.append(drum.A)
  return vecini
  
def getVeciniSiDist(oras):
  global drumuri
  vecini = []
  for drum in drumuri:
    if drum.A == oras:
      vecini.append((drum.B,drum.dist))
    if drum.B == oras:
      vecini.append((drum.A,drum.dist))
  return vecini
 
def searchSolLargime(nod_init, stare_fin):
  # se expandeaza nodul cu adancimea c m mica
  front = [nod_init]
  
  while len(front)>0:
    nod = front[0]
    if nod.stare == stare_fin:
      print (f'Solutia este: {nod.predecesori},{nod.stare}')
      return
    
    vecini = getVecini(nod.stare)
    
    for v in vecini:
      nod_next = Nod(v, nod.predecesori + (nod.stare,), nod.d+1, 0)
      front.append(nod_next)
    
    del(front[0])
    
  print('Nu exista solutie')
  
def searchSolAdancime(nod_init, stare_fin):
  # se expandeaza nodul cu adancimea c m mare
  front = [nod_init]
  n=0
  while len(front)>0 and n<10:
    #nod = front[len(front)-1]
    #del(front[len(front)-1])
    nod = front.pop(-1)
    
    print(f'Nod: {nod}')
    print(f'Frontiera: {front}')
    
    if nod.stare == stare_fin:
      print (f'Solutia este: {nod.predecesori},{nod.stare}')
      return
    
    vecini = getVecini(nod.stare)
    
    for v in vecini:
      nod_next = Nod(v, nod.predecesori + (nod.stare,), nod.d+1, 0)
      if nod_next not in nod.predecesori:
        front.append(nod_next)
  
    n=n+1

    
  print('Nu exista solutie')
  

## citere drumuri din fisier 
locatie_fisier = "D:\\work\\1404B\\map_input.txt"
numar_orase, drumuri = citire_date_din_fisier(locatie_fisier)
numar_drumuri = len(drumuri)

print(drumuri)
drum = drumuri[0]
print(drum.A, " <-> ", drum.B, " :",drum.dist)

stare_initiala = "Arad"
stare_finala = "Bucuresti"
nod_initial = Nod(stare_initiala, [], 0, 0)
print(nod_initial)

print ('Vecinii orasului Sibiu:')
vecini = getVecini('Sibiu')
print(vecini)

searchSolLargime(Nod('Neamt',(),0,0),'Drobeta')
searchSolAdancime(Nod('Sibiu',(),0,0),'Arad')
