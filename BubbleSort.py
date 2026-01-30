from colorama import Fore
def Swap(arr , a , b):
    arr[a] , arr[b] = arr[b] , arr[a]

def BubbleSort(arr , n):
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            Swap(arr , i , i + 1)
    BubbleSort(arr , n-1)

arr = [7 , 0 , 5 , -1 , 3 , 2 , 4]
BubbleSort(arr , len(arr))
print(Fore.GREEN + "The array is successfully sorted:", arr)