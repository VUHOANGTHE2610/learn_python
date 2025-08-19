#mảng 1 chiều
arr1 = [1, 2, 3]

#mảng 2 chiều
arr2 = [
    [4, 5, 6],
    [4, 1, 6],
    [4, 5, 6],
]
print(arr2[1][1]) #1
for row in arr2:
    for col in row:
        print(col)