def howmany(array,target):
    count = 0
    for n in array:
        if n ==target:
            count += 1
    return count
array= list(map(int, input("Enter a sequence of numb: ").split()))
target = int(input("Enter a number to be searched: "))
print(howmany(array,target))