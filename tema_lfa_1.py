#stochez graful intr-un dictionar de dictionare de tipul {noduri_curente : {muchii : [lista_noduri_urmatoare]}}.
#fisierul text trebuie sa citeasca pe prima linie starile finale (de tipul qi), 
#iar pe liniile urmatoare nodul curent, muchia si nodul la care ajunge prin muchia respectiva.
#momentan doar accepta/respinge cuvantul. trebuie sa afisez si drumurile.
#merge si pt DFA si pt NFA
d = {}
f = open("input.txt", "r")
s = f.readline()
stari_finale = s.split()
s = f.readline()
while s!= "":
    s = s.split()
    if s[0] not in d:
        d[s[0]] = {s[1] : [s[2]]}
    else:
        if s[1] not in d[s[0]]:
            d[s[0]][s[1]] = [s[2]]
        else: 
            d[s[0]][s[1]].append(s[2])
    s = f.readline()
f.close()

stari_curente = ["q0"]
drumuri = [["q0"]]
x =input("dati sirul: ")
for i in range (len(x)): #parcurg cuvantul
    L = []
    for j in stari_curente:
        if x[i] in d[j]: #daca exista ramuri pe care poate merge caracterul curent
            L.extend(d[j][x[i]]) #noile bifurcatii la starea curenta
    stari_curente = L.copy()
    if stari_curente == []:
        print('nu')
        break
else:
    for i in stari_finale:
        if i in stari_curente:
            print("da")
            break
    else:
        print('nu')

