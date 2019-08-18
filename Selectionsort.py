#!usr/bin/python

arr=[11,10,1,9,8,7,15,45,34,32]

print(arr)
for i in range(len(arr)):
	pos=i
	for j in range(i,len(arr)):
		if arr[j]<arr[pos]:
			pos=j
	(arr[i],arr[pos])=(arr[pos],arr[i])

print(arr)