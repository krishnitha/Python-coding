# Python program to split array and move first
# part to end.
 
def splitArr(arr, n, k): 
    for i in range(0, k): 
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
         
        arr[n-1] = x
         
 
# main
arr1 = [12, 10, 5, 6, 52, 36]
n1 = len(arr1)
k1 = 2

arr2 = [3, 1, 2]
n2 = len(arr2)
k2 = 1

print('before splitting \narr1 = ')
for i in range(0, n1): 
    print(arr1[i], end = ' ')
print('\n')
    
splitArr(arr1, n1, k1)

print('after splitting \narr1 = ' )
for i in range(0, n1): 
    print(arr1[i], end = ' ')
print('\n')
    
print('before splitting \narr2 = ')
for i in range(0, n2): 
    print(arr2[i], end = ' ')
print('\n')
    
splitArr(arr2, n2, k2)

print('after splitting \narr2 = ')
for i in range(0, n2): 
    print(arr2[i], end = ' ')

 
#
