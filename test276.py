#1
def add(first, second):         #함수 헤더     (매개변수1, 매개변수2)
    return first + second       #함수 보디

print(add(3,2))                 #print(리턴값)  (인수1, 인수2)


#2
def no_return():
    pass

def no_return_value():
    return

print(no_return())
print(no_return_value())


#3
def print_elements(arg):
    for x in arg:
        print(x)

print_elements(["Sun", "is", "rising"])

#4
def power(base, exp):
    return base ** exp

print(power(3, 2))
print(power(10, -2))

#5
def square(dataset):
    result = []
    for x in dataset:
        result.append(x * x)
    return result

print(square([3, 2, 5]))
print(square([323, 60]))


#6
def dict_to_list(dataset):
    result = []
    for x in dataset:
        result.append([x, dataset[x]])
    return result

data = {"my_key" : "my_value", "your_key" : "your_value"}
print(dict_to_list(data))


#7
def count_down(number):
    result = []
    for x in range(number):
        result.append(number - x)
    return result

print(count_down(10))
