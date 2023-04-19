filename='ListaVoti.txt'
x=float(0)
y=float(0)
with open(filename) as file:
    for line in file:
        voti=float(line.rstrip())
        print("voto:",voti)
        x=x+voti
        y=y+1
media=x/y

print("La media degli alunni è:",media,)

