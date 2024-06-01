#p222 ~ 224

msg = "혼자 공부하는 첫 프로그래밍"

print(msg)
print(msg[0])
print(msg[0:2])

print("========" * 20)

print(323)
print(type(323))
print(5.23)
print(type(5.23))
print(0.1 + 0.2 == 0.3)
print(0.1 + 0.2)
print(0 == "0")
print(type("0"))

print("========" * 20)

print(True)
print(False)
print(True == True)
print(True == "True")
print(type(True))
print(type("True"))

print("========" * 20)

book_list = ["혼자 공부하는 첫 프로그래밍", "혼자 공부하는 파이썬"]
count_down = [10,9,8,7,6,5,4,3,2,1]
print(type(book_list))

print("========" * 20)

book_dic = { "입문자" : "혼자 공부하는 첫 프로그래밍", "초보자" : "혼자 공부하는 파이썬"}
print(book_dic)
print(type(book_dic))

print("========" * 20)

count = range(3)
for x in count:
    print(x)

print("========" * 20)

#p225 문자열 데이터 셋트로 for문 돌리기.

string = "혼공족"
for char in string:
    print(char)
    print(type(char))
    print(type(string))