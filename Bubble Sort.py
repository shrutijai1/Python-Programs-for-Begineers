array = [13,21,43,2431,24,645,22,1]

for i in range(0,len(array)):
    for j in range(0,len(array)-i-1):
        if array[j]>array[j+1]:
            temp = array[j+1]
            array[j+1] = array[j]
            array[j] = temp
        

print(array)