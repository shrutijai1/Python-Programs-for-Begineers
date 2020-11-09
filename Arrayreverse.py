############ How to reverse an array ####################
"""
logic behind this problem is : 
we need to swap first element of an array into last element of an array and in the same way we need to second 
element from the left side swap with the last second element of an arrary
"""

def reversearray(givenarray,start,end):
    while start < end:
        givenarray[start],givenarray[end] = givenarray[end], givenarray[start]
        """
        we can not go like this because we need to perform this logic simultaneously at both end
        givenarray[start] = givenarray[end]
        givenarray[end] = givenarray[start]
        """
        start += 1
        end -= 1

givenarray = [23,54,12,545,343,454,145,213,1212]
print("Given array is",givenarray)
end  = len(givenarray) - 1
start = 0
reversearray(givenarray,start,end)
print("Reverse array is",givenarray)
