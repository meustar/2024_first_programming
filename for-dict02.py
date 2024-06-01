book_list = ["혼자 공부하는 첫 프로그래밍", "혼자 공부하는 파이썬"]
for book in book_list:
    print(book)

print("========" * 20)

book_dict = {
    "입문자용" : "혼자 공부하는 첫 프로그래밍", 
    "초보자용" : "혼자 공부하는 파이썬"
}
for book in book_dict:
    print(book)


print("========" * 20)


book_dict = {
    "입문자용" : "혼자 공부하는 첫 프로그래밍", 
    "초보자용" : "혼자 공부하는 파이썬"
}
for book in book_dict:
    print(book_dict[book])
