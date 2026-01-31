def Swap(arr , a  , b):
    arr[a] , arr[b] = arr[b] , arr[a]

def Partition(arr , debut , fin):
    pivot = fin
    i = (debut - 1)
    for j in range(debut , fin):
        if arr[j] < arr[pivot]:
            i+=1
            Swap(arr , i , j)
    Swap(arr , i+1 , fin)
    return i+1

def QuickSort(arr , debut , fin):
    if debut < fin:
        pivot = Partition(arr , debut , fin)
        QuickSort(arr , debut , pivot - 1)
        QuickSort(arr , pivot + 1 , fin)


arr = [8 , 2 , 1 , 0 , 1]
QuickSort(arr , 0 , 4)
print(arr)
