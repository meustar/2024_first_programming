opening = 54700
closing = 54700
diff = closing - opening
if diff > 0:
    print("↑" + str(diff))          #str 숫자를 문자로 변환
elif diff < 0:                      
    print("↓" + str(abs(diff)))     #abs 숫자데이터의 절댓값
else:
    print("-")