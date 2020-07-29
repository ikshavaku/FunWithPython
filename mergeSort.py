a=[12,3,11,65,43,76,1,34,27,2]

def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergeSort(left)
        mergeSort(right)

        leftidx=0
        rightidx=0
        mergedidx=0

        while leftidx<len(left) and rightidx<len(right):
            if left[leftidx] < right[rightidx]:
                arr[mergedidx]=left[leftidx]
                leftidx+=1
            else:
                arr[mergedidx]=right[rightidx]
                rightidx+=1
            mergedidx+=1
        while leftidx<len(left):
            arr[mergedidx]=left[leftidx]
            leftidx+=1
            mergedidx+=1
        while rightidx<len(right):
            arr[mergedidx]=right[rightidx]
            rightidx+=1
            mergedidx+=1

mergeSort(a)
print(a)