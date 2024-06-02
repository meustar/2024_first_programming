#1
def is_add(arg):
    if arg % 2 == 1:
        return True
    return False

print(is_add(3))
print(is_add(2))

#2
def get_sum_of_two_numbers(start, end):
    result = 0
    for x in range(start, end + 1):
        result = result + x
    return result

print(get_sum_of_two_numbers(1, 10))
print(get_sum_of_two_numbers(1, 100))

#3
def print_hashes(rows):
    for x in range(rows):
        print("#" * (x + 1))

print_hashes(3)

#4
def print_reverse_hashes(rows):
    for x in range(rows):
        count = x + 1
        print(" " * (rows - count) + "#" * count)

print_reverse_hashes(4)

#5
def replace_digits(str_):
    return str_[:9] + "****"

print(replace_digits("010-1234-5678"))
print(replace_digits("010-9876-5432"))

