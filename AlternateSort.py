#!usr/bin/python

#This program sorts an array in such a way that that the fielst element is the largest
#the secon element is the smallest,the third is the 2nd largest,4th is the second smallest
arr=[11,10,9,8,7,15,45,34,32,1]

print(arr)
for i in range(1,len(arr),2):
	pos=i
	maxp=i-1
	for j in range(i-1,len(arr)):
		if arr[j]<arr[pos]:
			pos=j
		if arr[j]>arr[maxp]:
			maxp=j
	(arr[i],arr[pos])=(arr[pos],arr[i])
	(arr[i-1],arr[maxp])=(arr[maxp],arr[i-1])
print(arr)