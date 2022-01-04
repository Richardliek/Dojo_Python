#1 countdown 

def countdown(num):
    output=[]
    for i in range(num,-1,-1):
        output.append(i)
    return output

print(countdown(10))

#2 print and return

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([2,3]))

#3

def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([5,6,7,8,9]))

#4

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output

print(values_greater_than_second([4,5,6,7,8]))
print(values_greater_than_second([3]))

#5

def length_and_value(size,value):
    output=[]
    for i in range(0,size):
        output.append(value)
    return output

print(length_and_value(6,9))
print(length_and_value(9,6))