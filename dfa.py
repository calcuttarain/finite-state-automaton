#citesc, din fisierul automat.in, pe prima linie, starile finale(separate prin spatii), apoi pe fiecare linie
#nodul, muchia si nodul la care ajunge prin muchia respectiva(separate tot prin spatii);
#salvez automatul intr-un dictionar de dictionare de forma keyStare:{keyMuchie:[listaStariUrmatoare]}.
import copy
d = {}
f = open('automat.in', 'r')
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

sir = input('Introduceti sirul: ')
drumuri = [['q0']]
for caracter in sir:
    drumuri_noi = []
    for drum in drumuri:
        stare = drum[len(drum)-1]
        if stare in d: #daca exista muchii pentru starea curenta
            if caracter in d[stare]: #daca exista muchia cu caracterul curent
                L = d[stare][caracter] #starile la care se ajunge la muchia respectiva
                for i in L: #adaug in alta lista drumurile la care adaug si starea urmatroare
                    aux = copy.deepcopy(drum)
                    aux.append(i)
                    drumuri_noi.append(aux)
    drumuri = copy.deepcopy(drumuri_noi) #actualizez lista de drumuri
    if drumuri == []: #daca niciun drum nu mai poate inainta
        print('NU ESTE ACCEPTAT!')
        break
else: #daca tot sirul e parcurs
    ok = 0
    i = 1
    for stare_finala in stari_finale: #afisam drumurile care se termina intr-o stare finala
        for drum in drumuri:
            if drum[len(drum)-1] == stare_finala:
                print(f'Drumul numarul {i}:')
                for j in range (len(drum)-1):
                    print(drum[j], end = '->')
                print (drum[len(drum)-1], end = '\n\n')
                i += 1
                ok = 1
    if ok == 0: #daca nu exista drumuri care sa se termine intr-o stare finala
        print('NU ESTE ACCEPTAT!')

