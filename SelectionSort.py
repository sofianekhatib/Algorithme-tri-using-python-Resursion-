from colorama import Fore
def FindMin(arr , debut , fin):
    min = debut
    for i in range(debut + 1 , fin):
        if arr[i] < arr[min]:
            min = i
    return min

def Swap(arr , a , b):
    arr[a] , arr[b] = arr[b] , arr[a]


def SelectionSort(arr , debut , fin):
    if debut >= fin - 1 :
        return
    minimun = FindMin(arr , debut , fin)
    Swap(arr , debut , minimun)
    SelectionSort(arr , debut + 1 , fin)
arr = [7 , 0 , 5 , -1 , 3 , 2 , 4]
SelectionSort(arr , 0 , len(arr))
print(Fore.GREEN + "The array is successfully sorted:", arr)



