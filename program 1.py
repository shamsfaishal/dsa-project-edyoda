#1.Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find(array, len, sum):
    print("Pairs whose sum is : ", sum)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == sum:
                print(array[i], array[j])


array = [5, 2, 3, 4, 1, 6, 7]

sum = 7

print("Array= ", array)

find(array, len(array), sum)
