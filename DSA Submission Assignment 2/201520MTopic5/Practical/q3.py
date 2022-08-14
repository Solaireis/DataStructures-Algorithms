def organized_recurse(data,low,high):
    if low < high:
        if data[high] % 2 == 0:  # data[high] is even

            # swapping of values (without temp variable)
            data[low],data[high] = data[high],data[low]

            # data[low] is known to be event
            organized_recurse(data,low+1,high)

        else:
            #data[high] is odd
            organized_recurse(data,low,high-1)

def organize(data):
    organized_recurse(data,0,len(data)-1)

orginallist = [1,2,3,4,5,6,7,8,9,10]
print(orginallist)
organize(orginallist)
print(orginallist)

#further imrpove by sorting it
#even number infront and sort it
