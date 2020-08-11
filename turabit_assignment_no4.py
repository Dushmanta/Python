import numpy as np

number_element = int(input("Please Enter the total number of list elelemnt  planning to enter: "))

list_element = list(map(str, input("\nPlease Enter the input list element with space : ").strip().split()))[:number_element]

res = []
for i in list_element:
    res.append(i)

arr = np.array(res)
print(set(map(lambda x: (x, list(arr).count(x)), arr)))
