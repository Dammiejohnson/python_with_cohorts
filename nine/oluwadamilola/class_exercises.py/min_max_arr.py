import sys
minimum = sys.maxsize
maximum = -sys.maxsize
total = 0

arr = [1,3,5,7,9]

for i in range(len(arr)):
    total += arr[i]
    if arr[i] < minimum:
        minimum = arr[i]
    if arr[i] > maximum:
        maximum = arr[i]
    maximum_total = total - minimum
    minimum_total = total - maximum
        
print(minimum_total, maximum_total)


