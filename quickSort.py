a=[12,4,5,67,21,14,32,98,3,27]

def quickSort(arr,first,last):
    if first<last:
        pivot=partition(arr,first,last)
        quickSort(arr,first,pivot-1)
        quickSort(arr,pivot+1,last)

def partition(arr,first,last):
    lower=first+1
    upper=last
    Done=False

    while Done !=True :
        while upper>=lower and arr[lower]<=arr[first]:
            lower+=1
        while upper>=lower and arr[upper]>=arr[first]:
            upper-=1
        if upper<lower:
            Done=True
        else:
            arr[upper],arr[lower]=arr[lower],arr[upper]
    arr[upper],arr[first]=arr[first],arr[upper]
    return upper

print(a)
quickSort(a,0,len(a)-1)
print(a)