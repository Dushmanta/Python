
n = int(input("Enter number of elements : "))

a = list(map(int ,input("\nPlease Enter the list element with space : ").strip().split()))[:n]
print("\nInput List is before removing duplicates- ", a)

res = []
for i in a:
    if i not in res:
        res.append(i)

print("The list after removing duplicates : " + str(res))