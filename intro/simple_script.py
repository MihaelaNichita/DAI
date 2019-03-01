lab_siad = "SIAD"

def salut():
    print('Hello:')
    
    nume_lab = input("What lab are we having now?\n")
    
    if nume_lab.upper() == lab_siad:
        print(f"Right! We are having {nume_lab.upper()}")
    else:
        print(":("+" Wrong!")
     
salut()

# if __name__=='__main__':
#    salut()