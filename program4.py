#4.Write a program to print the first non-repeated character from a string?
String = "sriharshareddy"
for i in String:
    count = 0
    for j in String:
        if i == j:
            count+=1
        if count > 1:
            break
    if count == 1:
        print(i,end = " ")
