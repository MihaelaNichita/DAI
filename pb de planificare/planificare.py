from collections import namedtuple

Nod = namedtuple("Nod", ['stare', 'actiuni', 'd', 'g', 'h', 'f'])
Stare = namedtuple('Stare',['poz_rob','pe_cutie', 'poz_cutii','lumini'])

DA='DA'
NU='NU'


def opUrcare(s):
    if s.pe_cutie == NU:
        return

    camere = [1,2,3]
    if s.poz_rob != None:
        camere = [s.poz_rob]

    preds = []
    for cam in camere:
        cutii = s.poz_cutii[:]
        cutii[cam-1] = DA
        s_pred = Stare(cam,NU,cutii,s.lumini[:])
        preds.append((s_pred,f"Urcare pe cutie in camera {cam}"))
    return preds


def opCoboara(s):
    if s.pe_cutie == DA:
        return

    camere =[e for e in [1,2,3] if s.poz_cutii[e-1] in [DA,None]] 
    if s.poz_rob != None:
        camere = [s.poz_rob]

    preds = []
    for cam in camere:
        cutii = s.poz_cutii[:]
        cutii[cam-1] = DA
        s_pred = Stare(cam,DA,cutii,s.lumini[:])
        preds.append((s_pred,f"Coborare de pe cutie in camera {cam}"))

    return preds


def opDeplasare(s):
    if s.pe_cutie == DA:
        return

    camere = [1,2,3]
    if s.poz_rob != None:
        camere = [s.poz_rob]

    preds = []
    for cam in camere:
        camere_pred = [e for e in [1,2,3] if e!=cam]

        s_pred1 = Stare(camere_pred[0],NU,s.poz_cutii[:],s.lumini[:])
        s_pred2 = Stare(camere_pred[1],NU,s.poz_cutii[:],s.lumini[:])

        preds.append((s_pred1,f"Deplasare din camera {camere_pred[0]} in camera {cam}"))
        preds.append((s_pred2,f"Deplasare din camera {camere_pred[1]} in camera {cam}"))
    return preds


def opMutaCutia(s):
    if s.pe_cutie == DA:
        return

    camere = [e for e in [1,2,3] if s.poz_cutii[e-1] in [None,DA]]

    if s.poz_rob != None:
        camere = [s.poz_rob]

    preds = []
    for cam in camere:
        poz_cutii = s.poz_cutii[:]
        poz_cutii[cam-1] = NU
        s_pred = Stare(cam,NU,poz_cutii[:],s.lumini[:])
        preds.append((s_pred,f"Mutare cutie langa intrerupator in camera {cam}"))
    return preds


def opLuminare(s):
    if s.pe_cutie == NU:
        return

    camere = [e for e in [1,2,3] if s.poz_cutii[e-1] in [None,DA] and s.lumini[e-1] in [None,DA]]

    if s.poz_rob != None:
        camere = [s.poz_rob]

    preds = []
    for cam in camere:
        lumini = s.lumini[:]
        lumini[cam-1] = NU
        s_pred = Stare(cam,DA,s.poz_cutii[:],lumini[:])
        preds.append((s_pred,f"Luminare camera {cam}"))
    return preds


def exp(stare):
    stari=[]

    ol=opLuminare(stare)
    if ol != None:
        stari.extend(ol)
    od=opDeplasare(stare)
    if od != None:
        stari.extend(od)
    ou=opUrcare(stare)
    if ou != None:
        stari.extend(ou)
    oc=opCoboara(stare)
    if oc != None:
        stari.extend(oc)
    om=opMutaCutia(stare)
    if om != None:
        stari.extend(om)

    return stari

    
def sect_dupa_largime(frontiera):
    nod = frontiera[0]
    del frontiera[0]
    return nod


def camp_inclus(camp1, camp2):
    return camp2 == None or camp1==camp2 or camp1==None


def lst_inclus(lst1, lst2):
    for i in range(len(lst1)):
        if not camp_inclus(lst1[i], lst2[i]):
            return False
    return True


def stare_inclus(s1, s2):
    for i in range(len(s1)):
        if (type(s1[i]) is list):
            if (not lst_inclus(s1[i], s2[i])):
                return False
        else:
            if (not camp_inclus(s1[i], s2[i])):
                return False
    return True


def cautare(nod_init, sf, sect_dupa):

  front = [nod_init]
  noduri_expandate = []
  count=0
  while len(front)>0:    
    nod = sect_dupa(front)

    if nod not in noduri_expandate:
        noduri_expandate.append(nod)
    count+=1

    if stare_inclus(nod.stare,sf) == True:
      print (f'Solutia data in {count} pasi este: {nod.actiuni}')
      return
            
    stari_urmatoare = exp(nod.stare)
        
    for s,actiune in stari_urmatoare:
        if s not in (e.stare for e in noduri_expandate):     
            g=nod.g+1
            nod_next = Nod(s, (actiune,) + nod.actiuni, nod.d+1,g, 0, 0)
            front.append(nod_next)


si = Stare(2,NU,[DA,None,NU],[None,NU,DA])
sf = Stare(1,DA,[DA,None,DA],[DA,DA,None])

nod_initial = Nod(sf, (), 0, 0, 0, 0)

cautare(nod_initial,si,sect_dupa_largime)

