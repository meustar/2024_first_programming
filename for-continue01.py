# count = range(10)

# for n in count:
#     if (n + 1) % 3 != 0 :
#         continue

#     print(str(n + 1) + "!")

# 마무리 문제 p217~219
#1
count = 5
while count >= 0 :
    print(str(count) + "!")
    count = count - 1

print("========" * 20)
#2
count = [5,4,3,2,1]
for x in count:
    print(str(x) + "!")

print("========" * 20)
#3
count = range(10)
for n in count:
    if (n + 1) % 3 == 0 :
        print("짝!")
    else:
        print(n + 1)

print("========" * 20)

#4
words = ["혼자", "공부하는", "첫", "프로그래밍", "!"]
for x in words:
    if x == "첫":
        print("첫 프로그래밍!")
        break
    print(x)

print("========" * 20)

#5
count = range(20)
for x in count:
    if ((x + 1) % 10) != 0:
        continue
    print(str(x + 1) + "!")