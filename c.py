
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))
k = int(input("Enter maximum elements to choose (k): "))


maximum_sum = 0


arr.sort(reverse=True)


for i in range(min(n, k)):
    if arr[i] > 0:
        maximum_sum += arr[i]
    else:
        break  

# Output
print(maximum_sum)
