from colorama import Fore

def Swap(arr , a , b):
    arr[a] , arr[b] = arr[b] , arr[a]

def Insert(arr , n):
    i = n - 2
    while i >= 0 and arr[i] > arr[i + 1]:
        Swap(arr , i + 1 , i)
        i = i - 1

def InsertionSort(arr , n):
    if n > 1:
      InsertionSort(arr , n - 1)
      Insert(arr , n)

arr = [7 , 0 , 5 , -1 , 3 , 2 , 4]
InsertionSort(arr , len(arr))
print(Fore.GREEN + "The array is successfully sorted:", arr)
