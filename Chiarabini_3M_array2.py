voti = []

file = "ListaVoti.txt"
with open(file) as file:
    i = 0
    for line in file:
        voto = float(line.strip()) 
        voti.append(voto)

somma_voti = 0
for voto in voti:
    somma_voti += voto
media_voti = somma_voti / len(voti)
print("Voti degli studenti:")
for voto in voti:
    print(voto, end=" ")
print("\nMedia dei voti:", media_voti)