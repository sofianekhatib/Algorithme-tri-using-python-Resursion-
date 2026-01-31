def Merge(Tab, debut, milieu, fin):
    arr = [0] * (fin - debut + 1)

    gauche = debut
    droite = milieu + 1
    i = 0

    # Fusion normale
    while gauche <= milieu and droite <= fin:
        if Tab[gauche] <= Tab[droite]:
            arr[i] = Tab[gauche]
            gauche += 1
        else:
            arr[i] = Tab[droite]
            droite += 1
        i += 1

    # Reste gauche
    while gauche <= milieu:
        arr[i] = Tab[gauche]
        gauche += 1
        i += 1

    # Reste droite
    while droite <= fin:
        arr[i] = Tab[droite]
        droite += 1
        i += 1

    # Recopie dans Tab
    for j in range(len(arr)):
        Tab[debut + j] = arr[j]


def MergeSort(Tab, debut, fin):
    if debut < fin:
        milieu = (debut + fin) // 2
        MergeSort(Tab, debut, milieu)
        MergeSort(Tab, milieu + 1, fin)
        Merge(Tab, debut, milieu, fin)


arr = [7, 3, 6, 1]
MergeSort(arr, 0, len(arr) - 1)
print(arr)
