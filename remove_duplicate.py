#Non-repeat values for list of interger
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


# Driver Code
list1 = [1,2,3,3,1,2,8]
#print(Repeat(list1))
list2 = set(Repeat(list1))
list_to_set = set(list1)
print(list_to_set-list2)