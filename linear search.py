size = int(input("Enter the size of array: "))
array = list(map(int,input().strip().split()))
print(array)
search = int(input("Search for: "))

for i in range(size):
    if array[i] == search:
        print("Search element is found in array at",i+1,"th position" )
    #else:
    #   print("Search element is not found in array")4
    