#1
coffee = "플랫화이트"
for x in coffee:
    print(x)

print("======" * 20)

#2
count = [1,2,3,4,5,6,7,8,9,10]
for x in count:
    if x % 2 == 0:
        print(str(x) + "!")

print("======" * 20)

#3
five = range(5)
for x in five:
    print((x + 1) * 3)

print("======" * 20)

#4
order = ["아메리카노", "플랫 화이트", "화이트 초콜릿 모카"]
price = [3100, 4100, 4600]
for x in range(3):
    print(order[x] + " : " + str(price[x]))

print("======" * 20)

#5
scores = [990, 120]
print(scores[0])
print(scores[1])

scores = {
    "TOEIC" : 990,
    "TOEFL iBT" : 120
}
print(scores["TOEIC"])
print(scores["TOEFL iBT"])

print("======" * 20)

#6
order = ["아메리카노", "플랫 화이트", "화이트 초콜릿 모카"]
price = {
    "아메리카노" : 3100,
    "플랫 화이트" : 4100,
    "화이트 초콜릿 모카" : 4600
}

for x in order:
    print(x + " : " + str(price[x]))

print("======" * 20)

#7
numbers = [[1,2,3], [4,5,6]]

for row in numbers:             # [1,2,3]               /   [4,5,6]
    total = 0
    for x in row:               
        total = total + x       # 0 + 1 + 2 + 3 = 6     /   0+ 4 + 5 + 6
    print(total)                # 6                     /   15

print("======" * 20)

#8
menu = {
    "오늘의 커피"           : 2800,
    "아메리카노"            : 3100,
    "카푸치노"              : 3600,
    "화이트 초콜릿 모카"     : 4600,
    "플랫 화이트"           : 4100
}

my_order = {
    "플랫 화이트" : 2,
    "화이트 초콜릿 모카" : 1
}

for x in my_order:
    price = menu[x]
    qty = my_order[x]
    total = price * qty
    print(x + " " + str(qty) + " 잔, 합계 : " + str(total))