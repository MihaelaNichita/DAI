
# Laborator 3 - Metode de cautare
#     cautare in adancime, largime, de cost minim, cautare increment

import sys
from collections import namedtuple

Drum = namedtuple("Drum", ['A', 'B', 'dist'])
# fiecare nod contine: stare (oras), predecesori (orasele predecesoare), 
#    d (adancimea), g (costul caii de la nodul de start pana la nodul curent) 
Nod = namedtuple("Nod", ['stare', 'predecesori', 'd', 'g'])

estimare = {
"Arad": 366,
"Bucuresti": 0,
"Craiova": 160,
"Drobeta": 242,
"Fagaras": 172,
"Giurgiu": 77,
"Hirsova": 151,
"Eforie": 161,
"Iasi": 226,
"Lugoj": 244,
"Mehadia": 241,
"Neamt": 234,
"Oradea": 380,
"Pitesti": 100,
"Rimnicu_Valcea": 193,
"Sibiu": 253,
"Timisoara": 329,
"Urziceni": 80,
"Vaslui": 199,
"Zerind": 374}

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
      vecini.append((drum.B,drum.dist))
    if drum.B == oras:
      vecini.append((drum.A,drum.dist))
  return vecini
 

# in loc sa scriu o alta functie dupa largime:  
def dupa_Adancime(front):
    return front.pop(-1)     # se expandeaza nodul cu adancimea c m mare
    
def dupa_Largime(front):
    return front.pop(0)     # se expandeaza nodul cu adancimea c m mica
    
def cost_min(front):
    index_min = 0         # se expandeaza nodul cu costul cel mai mic
    nod_min = min(front,key=lambda nod:nod.g)
    index_min = front.index(nod_min)
    #print (f"Nodul cu cost minim: {nod_min}")
    return front.pop(index_min)


def greedy(front):
    index=0
    nod_h_min = min(front, key=lambda nod:estimare[nod.stare])
    index = front.index(nod_h_min)
    print (f"Nodul cu ESTIMARE minimA: {nod_h_min}")
    return front.pop(index)

def search(nod_init, stare_fin,dupa):
    front = [nod_init]

    count=0
    while len(front)>0:  
        #print(f"frontiera = {front}")     
        nod = dupa(front)
        count+=1
      
        if nod.stare == stare_fin:
            print (f'Solutia data in {count} pasi este: {nod.predecesori},{nod.stare},{nod.g}')
            return
            
        vecini = getVecini(nod.stare)
        
        for v,dist in vecini:
            if v not in nod.predecesori:
                #print (v,dist)
                g = dist + nod.g 
                nod_next = Nod(v, nod.predecesori + (nod.stare,), nod.d+1, g)
                front.append(nod_next)
            
    print('Nu exista solutie')


## citIre drumuri din fisier 
locatie_fisier = "E:\\projects\\DAI\\search\\map_input.txt"
numar_orase, drumuri = citire_date_din_fisier(locatie_fisier)
numar_drumuri = len(drumuri)
'''
print(drumuri)
drum = drumuri[0]
print(drum.A, " <-> ", drum.B, " :",drum.dist)

stare_initiala = "Arad"
stare_finala = "Bucuresti"
nod_initial = Nod(stare_initiala, [], 0, 0)
print(nod_initial)
'''
#print ('Vecinii orasului Sibiu:')
#vecini = getVecini('Sibiu')
#print(vecini)

search(Nod('Bucuresti',(),0,0),'Sibiu',dupa_Adancime)
search(Nod('Bucuresti',(),0,0),'Sibiu',dupa_Largime)
search(Nod('Bucuresti',(),0,0),'Sibiu',cost_min)
search(Nod('Bucuresti',(),0,0),'Sibiu',greedy)
