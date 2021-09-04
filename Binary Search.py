array = [12,24,35,56,69,70]


low = 0
high = len(array)-1
mid = len(array)//2
search = int(input("Search for: "))


if search == array[mid]:
    print("Search found at:",mid+1)
elif search > array[mid]:
    low = mid + 1
    for i in range(len(array)//2):
        if search == array[low]:
            print("Search found at:",low+1)
            break
        else:
            low = low + 1
else:
    high = mid - 1
    for i in range(len(array)//2):
        if search == array[low]:
            print("Search found at:",low+1)
            break
        else:
            low = low + 1
